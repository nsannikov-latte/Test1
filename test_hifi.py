"""Tests for hifi.resample_linear_1d."""

import unittest

from hifi import resample_linear_1d


class TestResampleLinear1D(unittest.TestCase):
    def test_empty_signal(self) -> None:
        self.assertEqual(resample_linear_1d([], 5), [])

    def test_non_positive_out_length(self) -> None:
        self.assertEqual(resample_linear_1d([1.0, 2.0], 0), [])
        self.assertEqual(resample_linear_1d([1.0, 2.0], -1), [])

    def test_single_sample_replicated(self) -> None:
        self.assertEqual(resample_linear_1d([7.5], 3), [7.5, 7.5, 7.5])

    def test_two_points_three_outputs(self) -> None:
        self.assertEqual(resample_linear_1d([0.0, 1.0], 3), [0.0, 0.5, 1.0])

    def test_endpoints_preserved_for_two_samples(self) -> None:
        y = resample_linear_1d([-2.0, 4.0], 5)
        self.assertAlmostEqual(y[0], -2.0)
        self.assertAlmostEqual(y[-1], 4.0)

    def test_out_length_one_returns_first_sample(self) -> None:
        self.assertEqual(resample_linear_1d([10.0, 20.0, 30.0], 1), [10.0])


if __name__ == "__main__":
    unittest.main()
