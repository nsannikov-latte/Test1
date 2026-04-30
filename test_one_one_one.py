import unittest
from one_one_one import one_one_one


class TestOneOneOne(unittest.TestCase):
    def test_one_one_one(self):
        """Test that one_one_one returns 111."""
        self.assertEqual(one_one_one(), 111)


if __name__ == "__main__":
    unittest.main()
