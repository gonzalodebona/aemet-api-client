import sys
import logging

from aemet.api.api_client import AemetAPIClient
from aemet.data.data_processing import DataProcessing

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Aemet(object):

    @staticmethod
    def aemet_antarctica_data(api_key, start_date, end_date, station_id, aggregation):
        """
        Main entry point for retrieving weather data from AEMET's Antarctica stations.

        Args:
            api_key (str): API key for accessing AEMET's API.
            start_date (str): Start date for the data retrieval period in 'AAAA-MM-DDTHH:MM:SSUTC' format
            end_date (str): End date for the data retrieval period in 'AAAA-MM-DDTHH:MM:SSUTC' format.
            station_id (str): ID of the meteorological measurement station.
            aggregation (str): Method of data aggregation.

        Returns:
            dict: Aggregated weather data.

        Raises:
            ValueError: If the provided station_id or aggregation is invalid.
        """
        try:
            # Ensure correct Meteo Measurement Station
            if station_id not in ['89070', '89064']:
                raise ValueError(
                    "Meteo Measurement Station not valid: Try 89070 for Meteo Station Juan Carlos I or "
                    "89064 for Meteo Station Gabriel de Castilla"
                )

            # Ensure correct data aggregation
            if aggregation not in ['None', 'Hourly', 'Daily', 'Monthly']:
                raise ValueError(
                    "Time Aggregation not valid: Try None, Hourly, Daily, Monthly"
                )
            logging.info(
                "Execution parameters: start_date: %s, end_date: %s, station_id: %s, aggregation: %s",
                start_date, end_date, station_id, aggregation
            )

            # Create an instance of the API client
            api_client = AemetAPIClient(api_key)

            # Build the complete API endpoint URL and fetch raw data.
            raw_data = api_client.get_antarctica_data(start_date, end_date, station_id)

            # Create Data object
            data_object = DataProcessing(raw_data)

            # Aggregate data
            aggregated_data = data_object.aggregate_antarctica_data(aggregation)
            logging.info("End of process")
            return aggregated_data
        except Exception as e:
            logging.error(f"Error: {e}")
            sys.exit(1)
