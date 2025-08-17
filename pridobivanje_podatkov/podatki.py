import os, json, time, requests

url = "https://api.wtatennis.com/tennis/players/ranked"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/139.0.0.0 Safari/537.36"
}

leta = range(2000, 2025)  # 2000–2024
strani = range(0, 5)     # 5 strani × 50 = 250 igralk na leto
pavza = 0.5


def prenesi_stran(datum, stran):
    """Funkcija prenese eno stran (50 igralk)"""
    parametri = {
        "page": stran,
        "pageSize": 50,
        "type": "rankSingles",
        "sort": "asc",
        "metric": "SINGLES",
        "name": "",
        "at": datum,
        "nationality": ""
    }
    odgovor = requests.get(url, params=parametri, headers=headers)
    odgovor.raise_for_status()
    return odgovor.json()


trenutna_mapa = os.path.dirname(__file__) # mapa v kateri je ta skripta
ime_datoteke = os.path.join(trenutna_mapa, "wta_500_igralk_vsa_leta.json")

if os.path.exists(ime_datoteke):
    with open(ime_datoteke, "r", encoding="utf-8") as dat:
        tekmovalke = json.load(dat)
else:
    tekmovalke = []

ze_leta = set()
for zapis in tekmovalke:
    if "leto" in zapis:
        ze_leta.add(zapis["leto"])

for leto in leta:
    if leto in ze_leta:
        print(f"{leto} je že v datoteki")
        continue

    datum = f"{leto}-12-30"
    for stran in strani:
        podatki = prenesi_stran(datum, stran)
        if not podatki:
            break

        for t in podatki:
            t["leto"] = leto
            
        tekmovalke.extend(podatki)
        print(f"{datum}, stran {stran}: dodanih {len(podatki)} tekmovalk")
        time.sleep(pavza)


with open(ime_datoteke, "w", encoding="utf-8") as dat:
    json.dump(tekmovalke, dat, ensure_ascii=False, indent=4)

print(f"Shranjeno {len(tekmovalke)} igralk v {ime_datoteke}")

import shrani
shrani.shrani_igralke(tekmovalke)



