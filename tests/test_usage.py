import unittest
from relay.usage import usage_summary

class TestUsage(unittest.TestCase):
    def test_partial_cache_hit(self):
        usage = {"input_tokens": 10, "output_tokens": 2, "cache_read_tokens": 4}
        self.assertEqual(usage_summary(usage), {
            "input": 10, "output": 2, "total": 12, "cached_input": 4,
        })
