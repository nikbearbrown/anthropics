import os
import unittest

import stats

LOG = os.path.join(os.path.dirname(__file__), "readings.log")


class TestAvgTemp(unittest.TestCase):
    def test_sample_log(self):
        readings = stats.read_log(LOG)
        self.assertAlmostEqual(stats.avg_temp(readings), 21.45)

    def test_small_list(self):
        readings = [{"temp": "20.0"}, {"temp": "22.0"}]
        self.assertEqual(stats.avg_temp(readings), 21.0)

    def test_empty_returns_none(self):
        self.assertIsNone(stats.avg_temp([]))

    def test_missing_temp_key_is_skipped(self):
        readings = [{"temp": "20.0"}, {"time": "10:00"}, {"temp": "22.0"}]
        self.assertEqual(stats.avg_temp(readings), 21.0)

    def test_non_numeric_temp_is_skipped(self):
        readings = [{"temp": "20.0"}, {"temp": "abc"}, {"temp": "22.0"}]
        self.assertEqual(stats.avg_temp(readings), 21.0)

    def test_nan_row_is_skipped(self):
        # Sensor dropout: log line carries temp=NaN and must not poison the mean.
        r = stats.parse("12:30  temp=NaN  humid=42")
        self.assertEqual(r["temp"], "NaN")
        readings = [{"temp": "20.0"}, r, {"temp": "22.0"}]
        self.assertEqual(stats.avg_temp(readings), 21.0)

    def test_infinity_is_skipped(self):
        readings = [{"temp": "20.0"}, {"temp": "inf"}, {"temp": "22.0"}]
        self.assertEqual(stats.avg_temp(readings), 21.0)

    def test_all_unusable_returns_none(self):
        readings = [{"temp": "NaN"}, {"temp": "abc"}, {}]
        self.assertIsNone(stats.avg_temp(readings))


if __name__ == "__main__":
    unittest.main()
