"""Tests for stats.avg_temp."""
import unittest

from stats import avg_temp, read_log


class AvgTempTests(unittest.TestCase):
    def test_simple_average(self):
        readings = [
            {"time": "09:00", "temp": "20.0", "humid": "45"},
            {"time": "10:00", "temp": "22.0", "humid": "44"},
        ]
        self.assertAlmostEqual(avg_temp(readings), 21.0)

    def test_single_reading(self):
        self.assertAlmostEqual(avg_temp([{"time": "09:00", "temp": "19.5"}]), 19.5)

    def test_matches_readings_log_fixture(self):
        readings = read_log("readings.log")
        expected = (20.4 + 20.9 + 21.3 + 21.7 + 21.9 + 22.1 + 22.0 + 21.8 + 21.4 + 21.0) / 10
        self.assertAlmostEqual(avg_temp(readings), expected)

    def test_skips_missing_temp(self):
        readings = [
            {"time": "09:00", "temp": "20.0"},
            {"time": "10:00", "humid": "44"},
            {"time": "11:00", "temp": "22.0"},
        ]
        self.assertAlmostEqual(avg_temp(readings), 21.0)

    def test_skips_unparseable_temp(self):
        readings = [
            {"time": "09:00", "temp": "20.0"},
            {"time": "10:00", "temp": "not-a-number"},
            {"time": "11:00", "temp": "22.0"},
        ]
        self.assertAlmostEqual(avg_temp(readings), 21.0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            avg_temp([])

    def test_all_invalid_raises(self):
        with self.assertRaises(ValueError):
            avg_temp([{"time": "09:00"}, {"time": "10:00", "temp": "x"}])


if __name__ == "__main__":
    unittest.main()
