import unittest
from relay.streaming import stream_text

class TestStreaming(unittest.TestCase):
    def test_timeout_before_open(self):
        attempts = []
        def open_stream():
            attempts.append(1)
            if len(attempts) == 1:
                raise TimeoutError("connecting")
            return ["ok"]
        self.assertEqual(list(stream_text(open_stream)), ["ok"])
        self.assertEqual(len(attempts), 2)
