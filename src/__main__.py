import sys

from src.api.api_client import AemetAPIClient


def main():
    """
    Main entry point of the aemet-api-client command line interface.
    """
    try:
        # Ensure correct number of command line arguments
        if len(sys.argv) != 6:
            raise ValueError(
                "Usage: python -m aemet_api_client <api_key> <start_date> <end_date> <center> <aggregation>"
            )

        # Extract command line arguments
        api_key, start_date, end_date, station_id, aggregation = sys.argv[1:]

        # Create an instance of the API client
        api_client = AemetAPIClient(api_key)

        # Build the complete API endpoint URL and fetch raw data.
        raw_data = api_client.get_antartica_data(start_date, end_date, station_id)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
