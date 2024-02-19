import sys
import logging

from src.api.api_client import AemetAPIClient
from src.data.data_processing import DataProcessing
from src.common import extract_antarctica_params

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """
    Main entry point of the aemet-api-client command line interface.
    """
    try:
        # Extracts command line arguments
        api_key, start_date, end_date, station_id, aggregation = extract_antarctica_params()
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


if __name__ == "__main__":
    antarctica_data = main()
