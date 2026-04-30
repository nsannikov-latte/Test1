import unittest
from two_two_two import two_two_two


class TestTwoTwoTwo(unittest.TestCase):
    def test_two_two_two(self):
        """Test that two_two_two returns 222."""
        self.assertEqual(two_two_two(), 222)


if __name__ == "__main__":
    unittest.main()
