import sys
import logging


def extract_antarctica_params():
    """
    Extracts command line arguments for Antarctica weather data extraction.

    Returns:
        tuple: A tuple containing extracted parameters:
            - api_key (str): API key for accessing the data.
            - start_date (str): Start date of data extraction (format: YYYY-MM-DD).
            - end_date (str): End date of data extraction (format: YYYY-MM-DD).
            - station_id (str): ID of the Meteo Measurement Station.
            - aggregation (str): Aggregation level for the data ('None', 'Hourly', 'Daily', or 'Monthly').

    Raises:
        ValueError: If incorrect number of command line arguments is provided.
        ValueError: If the provided Meteo Measurement Station ID is not valid.
        ValueError: If the provided data aggregation level is not valid.
    """
    try:
        # Extract command line arguments
        api_key, start_date, end_date, station_id, aggregation = sys.argv[1:]

        # Ensure correct number of command line arguments
        if len(sys.argv) != 6:
            raise ValueError(
                "Usage: python -m aemet_api_client <api_key> <start_date> <end_date> <station> <aggregation>"
            )

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

        return api_key, start_date, end_date, station_id, aggregation
    except ValueError as ve:
        logging.error(f"Error extracting parameters: {ve}")
        sys.exit(1)
