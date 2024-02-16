import requests


class AemetAPIClient:
    """
    A class for interacting with the AEMET API endpoint and fetching data.

    Args:
        api_key (str): An optional API key for authentication (if required).

    Methods:
        - __init__(self, api_key: str = None)
        - get_antartica_data(self, start_date: str, end_date: str, station_id: str) -> dict
        - fetch_antartica_data(self, endpoint: str) -> dict
    """

    def __init__(self, api_key: str = None):
        """
        Initialize the AEMET API Client.

        Args:
            api_key (str, optional): An API key for authentication (if required).
        """
        self.api_key = api_key

    def get_antartica_data(self, start_date: str, end_date: str, station_id: str) -> dict:
        """
        Fetch raw data from the AEMET API for a specific weather station in Antartica.

        Args:
            start_date (str): Start date in the format 'AAAA-MM-DDTHH:MM:SSUTC'.
            end_date (str): End date in the format 'AAAA-MM-DDTHH:MM:SSUTC'.
            station_id (str): Identifier for the weather station.

        Returns:
            dict: JSON response containing data.
        """
        try:
            # Create endpoint
            endpoint = self.build_antartica_endpoint(start_date, end_date, station_id)

            # Fetch raw data
            raw_data = self.fetch_antartica_data(endpoint)
            return raw_data
        except requests.RequestException as e:
            raise Exception(f"Error fetching data from API: {e}")
        except ValueError as ve:
            raise Exception(f"Error parsing API response: {ve}")

    @staticmethod
    def build_antartica_endpoint(start_date: str, end_date: str, station_id: str) -> str:
        """
        Build the complete API endpoint URL for Antartica weather data.

        Args:
            start_date (str): Start date in the format 'YYYY-MM-DD'.
            end_date (str): End date in the format 'YYYY-MM-DD'.
            station_id (str): Identifier for the weather station.

        Returns:
            str: Complete API endpoint URL.
        """
        base_url = "https://opendata.aemet.es/opendata"
        antartica_url = f"/api/antartida/datos/fechaini/{start_date}/fechafin/{end_date}/estacion/{station_id}"
        return base_url + antartica_url

    def fetch_antartica_data(self, endpoint: str) -> dict:
        """
        Fetch raw Antartica weather data from the specified API endpoint.

        Args:
            endpoint (str): Complete API endpoint URL.

        Returns:
            dict: JSON response containing data.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        try:
            # Download raw data
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            json_response = response.json()
            data_url = json_response.get('datos')
            if not data_url:
                raise ValueError("No 'datos' URL found in API response")
            raw_data_response = requests.get(data_url)
            raw_data_response.raise_for_status()
            return raw_data_response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching data from API: {e}")
