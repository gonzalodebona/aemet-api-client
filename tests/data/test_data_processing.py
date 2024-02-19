import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from src.data.data_processing import DataProcessing
from tests.utils import raw_antarctica_data_processing


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.raw_data = raw_antarctica_data_processing

    def test_aggregate_antarctica_data_hourly(self):
        from tests.utils import expected_agg_hourly

        # Create aggregated_data df
        data_object = DataProcessing(self.raw_data)
        aggregated_data = data_object.aggregate_antarctica_data('Hourly')

        # Compare the result with the expected aggregated data
        assert_frame_equal(aggregated_data, pd.DataFrame(expected_agg_hourly))

    def test_aggregate_antarctica_data_daily(self):
        from tests.utils import expected_agg_daily

        # Create aggregated_data df
        data_object = DataProcessing(self.raw_data)
        aggregated_data = data_object.aggregate_antarctica_data('Daily')

        # Compare the result with the expected aggregated data
        assert_frame_equal(aggregated_data, pd.DataFrame(expected_agg_daily))

    def test_aggregate_antarctica_data_montly(self):
        from tests.utils import expected_agg_monthly

        # Create aggregated_data df
        data_object = DataProcessing(self.raw_data)
        aggregated_data = data_object.aggregate_antarctica_data('Monthly')

        # Compare the result with the expected aggregated data
        assert_frame_equal(aggregated_data, pd.DataFrame(expected_agg_monthly))


if __name__ == '__main__':
    unittest.main()
