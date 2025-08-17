import os
import pandas as pd


def shrani_igralke(igralke):
    """Shrani vse podatke o igralkah v CSV in izračuna starost"""
    pot_csv = os.path.join(os.path.dirname(__file__), "wta_igralke.csv")
    tabela = pd.json_normalize(igralke, sep='.')

    tabela = tabela[[
        'player.id',
        'player.firstName',
        'player.lastName',
        'player.fullName',
        'player.countryCode',
        'player.dateOfBirth',
        'ranking',
        'points',
        'leto'
    ]]

    tabela = tabela.rename(columns={
        'player.id': 'id_igralke',
        'player.firstName': 'ime',
        'player.lastName': 'priimek',
        'player.fullName': 'polno_ime',
        'player.countryCode': 'drzava',
        'player.dateOfBirth': 'datum_rojstva',
        'ranking': 'rang',
        'points': 'tocke'
    })

    # Izračun starosti
    tabela['datum_rojstva'] = pd.to_datetime(tabela['datum_rojstva'], errors='coerce')
    tabela['datum_ranga'] = pd.to_datetime(tabela['leto'].astype(str) + '-12-30')
    tabela['starost'] = ((tabela['datum_ranga'] - tabela['datum_rojstva']).dt.days / 365.25).round(0).astype(int)
    tabela = tabela.drop(columns=['datum_ranga'])

    



    stolpci_vrstni_red = [
        "id_igralke",
        "ime",
        "priimek",
        "polno_ime",
        "drzava",
        "datum_rojstva",
        "starost",       
        "rang",
        "tocke",
        "leto"
    ]
    tabela = tabela[stolpci_vrstni_red]


    tabela.to_csv(pot_csv, index=False, encoding='utf-8')
    print(f"Podatki shranjeni v: {pot_csv}")
