import unittest
import sys

from src.common import extract_antarctica_params


class TestExtractAntarcticaParams(unittest.TestCase):

    def test_valid_arguments(self):
        # Simulate valid command line arguments
        sys.argv = ['main.py', 'api_key', '2020-02-15T13:30:00UTC', '2020-02-16T13:30:00UTC', '89070', 'Hourly']
        api_key, start_date, end_date, station_id, aggregation = extract_antarctica_params()
        self.assertEqual(api_key, 'api_key')
        self.assertEqual(start_date, '2020-02-15T13:30:00UTC')
        self.assertEqual(end_date, '2020-02-16T13:30:00UTC')
        self.assertEqual(station_id, '89070')
        self.assertEqual(aggregation, 'Hourly')

    def test_invalid_arguments(self):
        # Simulate invalid command line arguments
        sys.argv = ['script.py', 'api_key', '2024-01-01', '2024-01-31', '89070']
        with self.assertRaises(SystemExit):
            extract_antarctica_params()


if __name__ == '__main__':
    unittest.main()
