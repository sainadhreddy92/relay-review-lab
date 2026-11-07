import unittest
from relay.history import prepare

class HistoryReview(unittest.TestCase):
    def test_recent_pair(self):
        self.assertEqual(prepare(iter(["a", "b", "c"]), 2), ["b", "c"])

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            prepare(["a"], -1)
