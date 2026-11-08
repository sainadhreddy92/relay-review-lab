import unittest
from relay.history import prepare

class TestHistory(unittest.TestCase):
    def test_recent_pair(self):
        self.assertEqual(prepare(iter(["a", "b", "c"]), 2), ["b", "c"])

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            prepare(["a"], -1)

    def test_no_limit_keeps_every_message_in_order(self):
        self.assertEqual(prepare(["a", "b", "c"]), ["a", "b", "c"])

    def test_zero_limit_returns_empty_history(self):
        self.assertEqual(prepare(["a", "b", "c"], 0), [])

    def test_limit_of_one_keeps_newest(self):
        self.assertEqual(prepare(["a", "b", "c"], 1), ["c"])

    def test_limit_equal_to_length_keeps_all(self):
        self.assertEqual(prepare(["a", "b", "c"], 3), ["a", "b", "c"])

    def test_limit_above_length_keeps_all(self):
        self.assertEqual(prepare(["a", "b", "c"], 5), ["a", "b", "c"])

    def test_limit_on_empty_history(self):
        self.assertEqual(prepare([], 2), [])
        self.assertEqual(prepare([], 0), [])

    def test_input_list_is_untouched(self):
        messages = ["a", "b", "c"]
        result = prepare(messages, 1)
        result.append("d")
        self.assertEqual(messages, ["a", "b", "c"])

    def test_non_integer_limit_is_rejected(self):
        for limit in (1.5, "2", True):
            with self.subTest(limit=limit):
                with self.assertRaises(TypeError):
                    prepare(["a", "b"], limit)

    def test_negative_limit_does_not_consume_iterator(self):
        messages = iter(["a", "b"])
        with self.assertRaises(ValueError):
            prepare(messages, -1)
        self.assertEqual(list(messages), ["a", "b"])
