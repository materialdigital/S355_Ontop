from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

fileName = (
	BASE_DIR
	/ "S355_data"
	/ "charpy_test"
	/ "02_secondary_data"
	/ "Charpy_test_results.xlsx"
)

sheetName = "Charpy_test_results"
firstRow = 8
lastRow = 13
columns = {
	"lfd." : 0,
	"crosspiece_mm" : 1,
	"length_mm" : 2,
	"width_mm" : 3,
	"thickness_mm" : 4,
	"KV2_750_5_J" : 5
}

primaryDataDir =  (
		BASE_DIR
		/ "S355_data"
		/ "charpy_test"
		/ "01_primary_data"
)
primaryDataSheetName = "Tabelle1"
primaryFirstRow = 40
primaryKeyCol = 0
primaryDataFields = {
	"test_temp_C" : [7,5],
	"test_date" : [9,5]
}

longitudinal_orientation = {
    "KX1" : 0,
    "KX2" : 0,
    "KX3" : 0,
    "KY1" : 90,
    "KY2" : 90,
    "KY3" : 90
}