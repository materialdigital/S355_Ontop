from pathlib import Path

fileName = Path(r"C:\Users\landbeck\Desktop\ottr_r2rml\r2rml\S355_data\sonic_resonance_test\02_secondary_data\results_sonic_resonance_tests.xlsx")
sheetName = "Ergebnisse Gesamt Resonanz"
firstRow = 19
lastRow = 23
columns = {
	"lfd." : 0,
	"mass_g" : 1,
	"length_mm" : 2,
	"width_mm" : 3,
	"height_mm" : 4,
	"density_gpercm3" : 5,
	"ff_fk_Hz" : 6,
	"ff_hk_Hz" : 7,
	"E_fk_GPa" : 8,
	"E_hk_GPa" : 9,
	"E_MW_GPa" : 10,
	"ft_Hz" : 11,
	"G_GPa" : 12,
	"mu_fk" : 13,
	"mu_hk" : 14,
	"mu_MW" : 15
}

longitudinal_orientation = {
    "ERX1" : 0,
    "ERX2" : 0,
    "ERY1" : 90,
    "ERY2" : 90
}