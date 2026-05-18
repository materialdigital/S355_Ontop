import sonicResonanceSecondaryData as srData
import charpyData as chData
import tensileData as tData
import pyexcel as p
from pathlib import Path
import os
import sqlite3
#### generate tables from the specified columns map names ####
def generate_create_table(table_name, column_maps):
	col_defs = []

	# merge both dicts
	for col_dict in column_maps:
		for name in col_dict.keys():
			if name == "lfd.":
				continue
			if name == "test_date":
				continue
			col_defs.append(f"{name} REAL")

		sql = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
	id VARCHAR(16) PRIMARY KEY,
	test_date TEXT,
	metal_sheet TEXT,
	orientation REAL,
	{",\n\t".join(col_defs)}
);
		"""
	return sql
################################################################################
def populate_table(table_name, entries, orientation_data):
	for key, values in entries.items():
		# first create an entry with key as id
		id_string = f"INSERT INTO {table_name} (id) VALUES (?)"
		cursor.execute(id_string, (key,))
		# now fill the rest for this row
		for field, val in values.items():
			if val == '-' or val == '':
				continue
			insert_string = f"UPDATE {table_name} SET {field} = ? WHERE id = ?"
			cursor.execute(insert_string, (val, key))
		# now the angle to the rolling direction
		orientation_insert_string = f"UPDATE {table_name} SET orientation = ? WHERE id = ?"
		cursor.execute(orientation_insert_string, (orientation_data[key], key))

################################################################################
# opens a sheet in a xlsx file and extracts data from the excel table.
# Data is written into entries, a map of structure key : {col : data, ...}
# meaning of columns is specified by colMap and the table ranges from firstRow to lastRow. 
def get_basic_data(fileName, sheetName, colMap, firstRow, lastRow, entries):
	sheet = p.get_sheet(file_name = fileName, sheet_name = sheetName)
	for row in range(firstRow, lastRow + 1):
		entry = {}
		key = sheet[row, colMap["lfd."]]
		if not key:
			continue
		for col in colMap:
			if col == "lfd.":
				continue
			entry[col] = sheet[row, colMap[col]]
		entries[key] = entry
################################################################################
db_path = os.path.join(os.path.dirname(__file__), "s355.db")
sonic_resonance_entries = {}
charpy_entries = {}
tensile_entries = {}
#### Sonic resonance data ######################################################
get_basic_data(srData.fileName, srData.sheetName, srData.columns, 
							 srData.firstRow, srData.lastRow, sonic_resonance_entries)
#### Charpy data ###############################################################
## secondary data
get_basic_data(chData.fileName, chData.sheetName, chData.columns, 
							 chData.firstRow, chData.lastRow, charpy_entries)
## primary data
primaryDataFileNames = [str(file) for file in Path(chData.primaryDataDir).glob("*.xlsx")]
for fileName in primaryDataFileNames:
	sheet = p.get_sheet(file_name = fileName, sheet_name = chData.primaryDataSheetName)
	for r in range(sheet.number_of_rows()):
		key = sheet[r,0]
		if key in charpy_entries.keys():
			for cell in chData.primaryDataFields:
				row, col = chData.primaryDataFields[cell]
				# now it gets a little messy
				if cell == "test_temp_C": 
					charpy_entries[key][cell] = float(sheet[row,col][:-3].replace(',', '.'))
				else:
					charpy_entries[key][cell] = str(sheet[row, col])

################################################################################
#### Tensile Data ##############################################################
get_basic_data(tData.fileName, tData.sheetName, tData.columns, 
							 tData.firstRow, tData.lastRow, tensile_entries)
# Verformungskennwerte
sheet = p.get_sheet(file_name = tData.fileName, sheet_name = tData.sheetName2)
colMap = tData.columns2
for row in range(tData.firstRow2, tData.lastRow2 + 1):
	key = sheet[row, colMap["lfd."]]
	if not key:
		continue
	for col in colMap:
		if col == "lfd.":
			continue
		tensile_entries[key][col] = sheet[row, colMap[col]]
# Experiment Parameters
for exp_file, exp_sheets in tData.experimentSheets.items():
	fileName = tData.experimentDir.joinpath(exp_file)
	for s in exp_sheets:
		sheet = p.get_sheet(file_name = fileName, sheet_name = s)
		# first get respective id's for the sheet
		id_string_field = [3, 2]
		ids_list = sheet[id_string_field[0], id_string_field[1]].split(" / ")
		# now get the experiment data and fill the according entries
		for fieldName, field in tData.experimentFields.items():
			val = sheet[field[0], field[1]]
			if (fieldName == "test_temp_C") and (val == "RT"):
				val = 21.5
			elif (fieldName == "weggeschwindigkeit_mmpers") or (fieldName == "umschaltpunkt_PERCENT"):
				val = sheet[field[0],field[1]].split()[0]
				val = float(val.replace(",", "."))
			elif isinstance(val, str):
				val = sheet[field[0],field[1]].split()[0]
			for id in ids_list:
				tensile_entries[id][fieldName] = val

################################################################################

# create queries for tables work. Next fill the tables. We need to handle '-' and '' entries and fill NULL instead
tensile_table_string = generate_create_table("tensile_data", [tData.columns, tData.columns2, tData.experimentFields])
print(tensile_table_string)
charpy_table_string = generate_create_table("charpy_data", [chData.columns, chData.primaryDataFields])
print(charpy_table_string)
sr_table_string = generate_create_table("sonic_resonance_data", [srData.columns])
print(sr_table_string)

# add metal sheet to entries
for key in sonic_resonance_entries:
	sonic_resonance_entries[key]["metal_sheet"] = "sheet1"
for key in charpy_entries:
	charpy_entries[key]["metal_sheet"] = "sheet1"
for key in tensile_entries:
	tensile_entries[key]["metal_sheet"] = "sheet1"
# now that table creation queries are construction we need to fill them with the
# data from our charpy_entries, sonic_resonance_entries, tensile_entries
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# create tables (if not exist)
cursor.execute(tensile_table_string)
cursor.execute(charpy_table_string)
cursor.execute(sr_table_string)
# metal sheet table
sheet_table_string = f"""
CREATE TABLE IF NOT EXISTS sheet_data (
	id VARCHAR(16) PRIMARY KEY
);"""
cursor.execute(sheet_table_string)
sheet1_string = f"INSERT INTO sheet_data (id) VALUES ('sheet1');"
cursor.execute(sheet1_string)

# fill tables
populate_table("tensile_data", tensile_entries, tData.longitudinal_orientation)

conn.commit()
populate_table("charpy_data", charpy_entries, chData.longitudinal_orientation)
conn.commit()
populate_table("sonic_resonance_data", sonic_resonance_entries, srData.longitudinal_orientation)
conn.commit()


cursor.close()
conn.close()
