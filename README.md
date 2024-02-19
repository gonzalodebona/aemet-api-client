# aemet-api-client

## Introduction
`aemet-api-client` is a Python library designed to facilitate access to AEMET (Agencia Estatal de Meteorología) API services. It provides functionalities to retrieve meteorological data from specific weather stations over defined time periods with customizable time aggregations.


## Prerequisites
In order to run this library you must have a validated API key from the AEMET and and have python 3.8 installed or above.


## Installation
To install aemet-api-client, you can use git clone:

```
git clone https://github.com/gonzalodebona/prueba.git
```

To install dependencies use:

```
pip install -r requirementst.txt
```

## Directory Structure
    * src/: Contains the source code of the library.
        * api/: Contains the API client class.
        * data/: Contains the data processing class.
        * common.py: Contains common functions. 
        * main.py: Entry point of the library.
    * test/: Contains unit tests for the library.
    * README.md: Documentation for the library.
    * requirements.txt: List of dependencies.
    * setup.py: Installation script.


## Parameters
The library allows the user to specify the following parameters:

    * API Key: An API key is required to access AEMET API services.
    * Datetime Start: Start datetime in the format YYYY-MM-DDTHH:MM:SSUTC.
    * Datetime End: End datetime in the format YYYY-MM-DDTHH:MM:SSUTC.
    * Meteo Measurement Station: Choose between "Meteo Station Gabriel de Castilla" and "Meteo Station Juan Carlos I".
    * Time Aggregation: Choose from None, Hourly, Daily, and Monthly.

**Important: To collect data from the station, the station ID codes must be:** <br>
**Meteo Station Gabriel de Castilla** -> **89070** <br>
**Meteo Station Juan Carlos I** -> **89064** <br>

## Granularity
    * The output dataset shall be aggregated based on the user selection of the Time Aggregation field.
    * The output dataset shall not be aggregated when None is selected.

## Output
The output dataset will be a dataframe that will have the following structure:

| Dataset Field Name | Description                   |
|--------------------|-------------------------------|
| Station            | Name of the station           |
| Datetime           | Date and time of the measurement |
| Temperature (ºC)   | Temperature in º Celsius       |
| Pressure (hpa)     | Pressure in hpa                |
| Speed (m/s)        | Wind speed in m/s              |

## Execution

```
python -m src <api_key> <start_date> <end_date> <station_id> <aggregation>
```

Example for Meteo Station Gabriel de Castilla:

```
python -m src eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkZWJvbmFnb256YWxvQGdtYWlsLmNvbSIsImp0aSI6IjUxMGNlMjEzLWYzYmUtNDY1MS1iZjlmLWZjNjMwMjVmNjRiMiIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA3ODM2ODg5LCJ1c2VySWQiOiI1MTBjZTIxMy1mM2JlLTQ2NTEtYmY5Zi1mYzYzMDI1ZjY0YjIiLCJyb2xlIjoiIn0.0KUZveBVA9r72H8Xg-T4_0xMb5iJEaeLpXz0d6ecSnY 2010-02-14T13:30:02UTC 2010-03-14T18:45:00UTC 89070 Monthly
```

## Testing

```
python -m unittest
```