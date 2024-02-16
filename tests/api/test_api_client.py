import unittest
from unittest.mock import Mock, patch

from src.api.api_client import AemetAPIClient


class TestAemetAPIClient(unittest.TestCase):

    def setUp(self):
        self.api_key = "YOUR_API_KEY"
        self.client = AemetAPIClient(self.api_key)

    def test_build_antartica_endpoint(self):
        from tests.utils import antartica_endpoint
        start_date = "2010-02-14T13:30:00UTC"
        end_date = "2010-02-14T13:45:00UTC"
        station_id = "89070"
        endpoint = self.client.build_antartica_endpoint(start_date, end_date, station_id)
        self.assertEqual(endpoint, antartica_endpoint)

    @patch('src.api.api_client.requests.get')
    def test_fetch_antartica_data(self, mock_get):
        # Import synthetic data for testing.
        from tests.utils import antartica_endpoint, antartica_json_data, antartica_api_response, raw_antartica_data

        # Create a mock API response object.
        mock_api_response = Mock()
        mock_api_response.json.return_value = antartica_api_response

        # Create a mock data response object.
        mock_data_response = Mock()
        mock_data_response.json.return_value = raw_antartica_data

        mock_get.side_effect = [mock_api_response, mock_data_response]
        raw_antartica_data_real = self.client.fetch_antartica_data(antartica_endpoint)

        # Test request methods
        mock_get.assert_any_call(antartica_endpoint, headers={"Authorization": f"Bearer {self.api_key}"})
        mock_get.assert_any_call(antartica_json_data)
        self.assertEqual(raw_antartica_data_real, raw_antartica_data)
