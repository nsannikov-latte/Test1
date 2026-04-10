"""Tests for triple_three.triple_three."""

import unittest

from triple_three import triple_three


class TestTripleThree(unittest.TestCase):
    def test_returns_333(self) -> None:
        self.assertEqual(triple_three(), 333)


if __name__ == "__main__":
    unittest.main()
