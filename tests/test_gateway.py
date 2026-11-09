import unittest
from relay import respond

class RecordingProvider:
    usage = {"input_tokens": 4, "output_tokens": 1}

    def __init__(self):
        self.seen = []

    def open(self, history):
        self.seen.append(history)
        return iter(["ok", ""])

class TestGatewayHistoryLimit(unittest.TestCase):
    def test_limit_bounds_history_sent_to_provider(self):
        provider = RecordingProvider()
        result = respond(provider, ["a", "b", "c"], limit=2)
        self.assertEqual(provider.seen, [["b", "c"]])
        self.assertEqual(result, {
            "text": "ok", "usage": {"input": 4, "output": 1, "total": 5},
        })

    def test_zero_limit_sends_empty_history(self):
        provider = RecordingProvider()
        respond(provider, ["a", "b"], limit=0)
        self.assertEqual(provider.seen, [[]])

    def test_default_sends_full_history(self):
        provider = RecordingProvider()
        messages = ["a", "b", "c"]
        respond(provider, messages)
        self.assertEqual(provider.seen, [["a", "b", "c"]])
        self.assertIsNot(provider.seen[0], messages)

    def test_negative_limit_fails_before_provider_is_opened(self):
        provider = RecordingProvider()
        with self.assertRaises(ValueError):
            respond(provider, ["a"], limit=-1)
        self.assertEqual(provider.seen, [])
