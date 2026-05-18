from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

fileName = (
	BASE_DIR
	/ "S355_data"
	/ "tensile_test"
	/ "02_secondary_data"
	/ "results_protocols"
	/ "tensile_test_results.xlsx"
)

sheetName = "Festigkeitskennwerte"
firstRow = 14 
lastRow = 26
columns = {
	"lfd." : 0,
	"d1_a1_mm" : 1,
	"d2_a2_mm" : 2,
	"d3_a3_mm" : 3,
	"b1_mm" : 4,
	"b2_mm" : 5,
	"b3_mm" : 6,
	"s1_mm2" : 7,
	"s2_mm2" : 8,
	"s3_mm2" : 9,
	"FeH_kN" : 14,
	"ReH_MPa" : 15, 
	"Fm_kN" : 16,
	"Rm_MPa" : 17,
	"E_GPa" : 18
}

sheetName2 = "Verformungskennwerte"
firstRow2 = 15 
lastRow2 = 26
columns2 = {
	"lfd." : 0,
	"L0_mm" : 1,
	"Lu_mm" : 2,
	"A_PERCENT" : 3,
	"au_mm" : 4,
	"bu_mm" : 5,
	"Su_mm2" : 8,
	"Z_PERCENT" : 9
}

experimentDir = Path(r"C:\Users\landbeck\Desktop\ottr_r2rml\r2rml\S355_data\tensile_test\02_secondary_data\results_protocols")
experimentDir = (
		BASE_DIR
		/ "tensile_test"
		/ "02_secondary_data"
		/ "results_protocols"
	)
experimentSheets = {
	Path(r"Protokoll-Zugversuch RT Zd.xlsx") : [r"Protokoll"],
	Path(r"Protokoll-Zugversuch RT Zx.xlsx") : [r"Protocol_Zx1", r"Protocol_Zx2_to_Zx4"],
	Path(r"Protokoll-Zugversuch RT Zy.xlsx") : [r"Protokoll"]
}
experimentFields = {
	"test_date" : [3,8],
	"test_temp_C" : [18,8],
	"dehngeschwindigeit_1perS" : [19, 2],
	"umschaltpunkt_PERCENT" : [20, 2],
	"weggeschwindigkeit_mmpers" : [21, 2]
}

longitudinal_orientation = {
    "Zx1" : 0,
    "Zx2" : 0,
    "Zx3" : 0,
    "Zx4" : 0,
    "Zy1" : 90,
    "Zy2" : 90,
    "Zy3" : 90,
    "Zy4" : 90,
    "Zd2" : 45,
    "Zd3" : 45,
    "Ax1" : 0
}