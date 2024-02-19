from typing import List, Dict
import pandas as pd
import logging


class DataProcessing:
    """
    A class for processing raw data from the Antarctica.

    Args:
        raw_data (List[Dict[str, any]]): A list of dictionaries representing raw data.

    Methods:
        - __init__(self, raw_data: List[Dict[str, any]])
        - aggregate_antarctica_data(self, aggregation: str) -> pd.DataFrame
    """

    def __init__(self, raw_data: List[Dict[str, any]]):
        """
        Initialize DataProcessing with raw data.

        Args:
            raw_data (List[Dict[str, any]]): A list of dictionaries representing raw data points.
                Each dictionary should have keys 'fhora' for timestamp and 'temp' for temperature value.
        """
        self.raw_data = raw_data

    def aggregate_antarctica_data(self, aggregation: str) -> pd.DataFrame:
        """
        Aggregate the raw data from the Antarctica based on the specified aggregation.

        Args:
            aggregation (str): The aggregation level ('None', 'Hourly', 'Daily', or 'Monthly').

        Returns:
            pd.DataFrame: Aggregated data where columns represent:
                - Station: Name of the station
                - Datetime: Date and time of the measurement
                - Temperature (ºC): Temperature in º Celsius
                - Pressure (hpa): Pressure in hpa
                - Speed (m/s): Wind speed in m/s
        Raises:
            Exception: If an error occurs during data aggregation.
        """
        try:
            # Filter only necessary columns
            cols_dataset = ['fhora', 'temp', 'pres', 'vel']
            filter_raw_data = [{key: d[key] for key in cols_dataset if key in d} for d in self.raw_data]

            # Convert raw data to DataFrame
            df_raw_data = pd.DataFrame(filter_raw_data)

            # Drop NaN values and duplicates
            df_raw_data = df_raw_data.replace('NaN', pd.NA).dropna().drop_duplicates()

            # Convert fhora to CET/CEST and set as index
            df_raw_data['fhora'] = pd.to_datetime(df_raw_data['fhora'])
            df_raw_data.set_index('fhora', inplace=True)

            # Resample based on aggregation level and calculate mean for numerical columns
            if aggregation != 'None':
                if aggregation == 'Hourly':
                    agg_freq = 'H'
                    datetime_format = '%Y-%m-%d %H:00:00'
                elif aggregation == 'Daily':
                    agg_freq = 'D'
                    datetime_format = '%Y-%m-%d'
                elif aggregation == 'Monthly':
                    agg_freq = 'M'
                    datetime_format = '%Y-%m'

                aggregated_data = df_raw_data.resample(agg_freq).mean()
                logging.info("Data aggregated %s", aggregation)
            else:
                # If aggregation is None, simply return the DataFrame without modification
                aggregated_data = df_raw_data
                logging.info("Data not aggregated")

            # Add 'Station' column with the station name
            aggregated_data['Station'] = self.raw_data[0]['nombre']

            # Rename columns
            aggregated_data.rename(
                columns={'temp': 'Temperature (ºC)', 'pres': 'Pressure (hpa)', 'vel': 'Speed (m/s)'}, inplace=True
            )

            # Reset index and format Datetime column
            aggregated_data.reset_index(inplace=True)
            # Format Datetime column
            aggregated_data['Datetime'] = aggregated_data['fhora'].dt.strftime(datetime_format)

            return aggregated_data[
                ['Station', 'Datetime', 'Temperature (ºC)', 'Pressure (hpa)', 'Speed (m/s)']
            ]
        except Exception as e:
            raise Exception(f"Error aggregating data: {e}")
