import unittest
from relay.tools import Tools

class TestTools(unittest.TestCase):
    def test_repeat_lookup(self):
        calls = []
        def fetch(catalog, item):
            calls.append((catalog, item))
            return "record"
        tools = Tools(fetch, clock=lambda: 0)
        self.assertEqual(tools.lookup("manual", "intro"), "record")
        self.assertEqual(tools.lookup("manual", "intro"), "record")
        self.assertEqual(len(calls), 1)
