# Projektna naloga - UVP
## Analiza igralk na WTA lestvici
Avtorica: Maria Šulek

Avgust 2025

### Uvod 
V tej analizi obravnavam WTA lestvico najboljših teniških igralk. Zajela sem podatke o najboljših 250 igralkah na WTA lestvici od leta 2000 do 2024. Namen analize je raziskati vzorce, ki se pojavljajo med igralkami.

Osredotočila sem se predvsem na dve vprašanji:

- Povprečna starost igralk – pričakujem, da se povprečna starost igralk v top 250 skozi čas zvišuje, enak trend pa velja tudi za starost igralk med najboljšimi desetimi.

- dodaj

Analizirala pa sem tudi: razlike v številu točk med najboljšimi 10 igralkami in ostalimi, obstojnost igralk med najboljšimi desetimi in na vrhu lestvice skozi čas ter pogostost imen igralk na WTA lestvici.

Vse podatke sem zajela iz spletne strani [WTA Tennis](https://www.wtatennis.com/rankings/singles).

### Potrebne knjižnice
Za zagon analize so potrebne naslednje knjižnice:
beautifulsoup, requests, os, csv, pandas, json, matplotlib.pyplot in time.

### Datoteke
- 'podatki.py' prenese podatke o WTA igralkah z uradne spletne strani in jih shrani v lokalno datoteko "wta_500_igralk_vsa_leta,json".
- 'shrani.py' podatke, podane v obliki JSON slovarjev s pomočjo knjižnice pandas preoblikuje v tabelo z informacijami o igralkah in jih shrani v datoteko "wta_igralke.csv".
- 'kontinenti.py' doda stolpec kontinent k obstoječi tabeli "wta_igralke.csv", tako da vsaki igralki določi, iz katere celine prihaja glede na njeno državo.
- 'analiza_podatkov.ipynb' prikazuje zaključeno analizo podatkov, dopolnjeno z grafi in histogrami.
