import unittest
from relay.gateway import respond
from relay.history import prepare
from relay.streaming import stream_text
from relay.tools import Tools
from relay.usage import usage_summary

class RelayTests(unittest.TestCase):
    def test_gateway(self):
        class Provider:
            usage = {"input_tokens": 3, "output_tokens": 2}
            def open(self, history):
                return iter(["hi", "", "!"])
        result = respond(Provider(), ["hello"])
        self.assertEqual(result["text"], "hi!")
        self.assertEqual(result["usage"]["total"], 5)

    def test_prepare_copies_outer_list(self):
        history = ["hi"]
        self.assertIsNot(prepare(history), history)
        self.assertEqual(prepare(history), ["hi"])

    def test_stream_ignores_empty_events(self):
        self.assertEqual(list(stream_text(lambda: ["", "x"])), ["x"])

    def test_lookup_calls_backend(self):
        tools = Tools(lambda catalog, item: f"{catalog}/{item}")
        self.assertEqual(tools.lookup("docs", "guide"), "docs/guide")

    def test_missing_usage_defaults(self):
        self.assertEqual(usage_summary({})["total"], 0)
