import pandas as pd
import os

kontinenti= {
    'Afrika': ['ALG', 'ANG', 'BUR', 'CAF', 'CGO', 'CIV', 'CMR', 'CPV', 'GAB', 'GAM', 'GBS', 'GHA', 'KEN',
    'MAR', 'MRI', 'NAM', 'NGR', 'RSA', 'SEN', 'SEY', 'SLE', 'STP', 'TOG', 'UGA'],
    'Azija': ['AZE', 'BAN', 'CHN', 'GEO', 'HKG', 'IND', 'IRI', 'IRQ', 'JPN', 'KAZ', 'KOR', 'KSA', 'KUW',
              'LBN', 'MAC', 'MNT', 'MON', 'PHI', 'SRI', 'THA', 'TKM', 'UAE'],
    'Evropa': ['ALB', 'AND', 'AUT', 'BEL', 'BIH', 'BLR', 'BUL', 'CRO', 'CYP', 'CZE', 'DEN', 'ESA', 'ESP',
               'EST', 'FIN', 'FRA', 'GBR', 'GER', 'GRE', 'HUN', 'IRL', 'ISL', 'ISR', 'ITA', 'KOS', 'LAT',
               'LIE', 'LTU', 'LUX', 'MDA', 'MKD', 'MLT', 'NED', 'NOR', 'POL', 'POR', 'ROU', 'RUS', 'SLO',
               'SMR', 'SRB', 'SUI', 'SVK', 'SWE', 'TUR', 'UKR'],
    'Južna Amerika': ['ARG', 'BOL', 'BRA', 'CHI', 'COL', 'ECU', 'GUY', 'PAR', 'PER', 'URU', 'VEN'],
    'Oceanija': ['AUS', 'FIJ', 'NZL', 'PNG', 'SOL'],           
    'Severna Amerika': ['AIA', 'ANT', 'BAH', 'BAR', 'BER', 'CAN', 'CAY', 'CRC', 'DOM', 'GRN',
                                   'GUA', 'HAI', 'IVB', 'JAM', 'LCA', 'MEX', 'PUR', 'SKN', 'TTO', 'USA', 'VIN'],
}

def doloci_kontinent(drzava, kontinenti):
    for kontinent, drzave in kontinenti.items():
        if drzava in drzave:
            return kontinent
        
mapa_skripte = os.path.dirname(__file__)         
        
tabela = pd.read_csv(os.path.join(mapa_skripte,'wta_igralke.csv'))

tabela['kontinent'] = tabela['drzava'].apply(lambda x: doloci_kontinent(x, kontinenti))

tabela.to_csv(os.path.join(mapa_skripte,'wta_igralke.csv'), index=False, encoding='utf-8') 