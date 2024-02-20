# file with synthetic data for the tests

# INPUTS
antarctica_json_data = 'https://opendata.aemet.es/opendata/sh/28682e36_202402161617_json'
antarctica_api_response = {
    'descripcion': 'exito',
    'estado': 200,
    'datos': 'https://opendata.aemet.es/opendata/sh/28682e36_202402161617_json',
    'metadatos': 'https://opendata.aemet.es/opendata/sh/2cc612ba'
}

raw_antarctica_data = {
    'identificacion': '89070', 'nombre': 'GdC Estacion meteorologica', 'latitud': -62.97697, 'longitud': -60.67528,
    'altitud': 12.0, 'srs': 'WGS84', 'alt_nieve': 0.0, 'ddd': 105, 'dddstd': 9, 'dddx': 93,
    'fhora': '2010-02-14T13:40:00', 'hr': 69, 'ins': 'NaN', 'lluv': 0.0, 'pres': 1006.4, 'rad_kj_m2': 0.0,
    'rad_w_m2': 293.4, 'rec': 0.0, 'temp': 1.6, 'tmn': 'NaN', 'tmx': 'NaN', 'ts': 2.9, 'tsb': 0.0, 'tsmn': 'NaN',
    'tsmx': 'NaN', 'vel': 3.2, 'velx': 4.8, 'albedo': 0.0, 'difusa': 0.0, 'directa': 0.0, 'global': 0.0,
    'ir_solar': 0.0, 'neta': 0.0, 'par': 0.0, 'tcielo': 0.0, 'ttierra': 0.0, 'uvab': 0.0, 'uvb': 0.0, 'uvi': 0.0,
    'qdato': 0
}

raw_antarctica_data_processing = [
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-02-29T23:00:00', 'temp': 10.0,
     'pres': 1200.0, 'vel': 5.0},
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-02-29T23:10:00', 'temp': 9.0,
     'pres': 1100.0, 'vel': 6.0},
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-02-29T23:20:00', 'temp': 8.0,
     'pres': 1200.0, 'vel': 5.5},
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-02-29T23:30:00', 'temp': 11.0,
     'pres': 1100.0, 'vel': 4.5},
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-03-01T00:20:00', 'temp': 8.0,
     'pres': 1200.0, 'vel': 5.5},
    {'nombre': 'Estación Meteorológica Gabriel de Castilla', 'fhora': '2024-03-01T00:30:00', 'temp': 11.0,
     'pres': 1100.0, 'vel': 4.5},
]

# OUTPUTS
antarctica_endpoint = "https://opendata.aemet.es/opendata/api/antartida/datos/fechaini/2010-02-14T13:30:00UTC" \
                     "/fechafin/2010-02-14T13:45:00UTC/estacion/89070"
expected_agg_hourly = {
    'Station': ['Estación Meteorológica Gabriel de Castilla', 'Estación Meteorológica Gabriel de Castilla'],
    'Datetime': ['2024-02-29 23:00:00', '2024-03-01 00:00:00'],
    'Temperature (ºC)': [9.5, 9.5],
    'Pressure (hpa)': [1150.0, 1150.0],
    'Speed (m/s)': [5.25, 5.0]
}

expected_agg_daily = {
    'Station': ['Estación Meteorológica Gabriel de Castilla', 'Estación Meteorológica Gabriel de Castilla'],
    'Datetime': ['2024-02-29', '2024-03-01'],
    'Temperature (ºC)': [9.5, 9.5],
    'Pressure (hpa)': [1150.0, 1150.0],
    'Speed (m/s)': [5.25, 5.0]
}

expected_agg_monthly = {
    'Station': ['Estación Meteorológica Gabriel de Castilla', 'Estación Meteorológica Gabriel de Castilla'],
    'Datetime': ['2024-02', '2024-03'],
    'Temperature (ºC)': [9.5, 9.5],
    'Pressure (hpa)': [1150.0, 1150.0],
    'Speed (m/s)': [5.25, 5.0]
}
