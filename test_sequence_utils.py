import unittest

from sequence_utils import chunked


class ChunkedTests(unittest.TestCase):
    def test_chunk_shapes_order_and_independence(self):
        cases = [
            ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
            ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
            ([1, 2], 1, [[1], [2]]),
            ([1, 2], 5, [[1, 2]]),
        ]
        for values, size, expected in cases:
            with self.subTest(values=values, size=size):
                original = values.copy()
                result = chunked(values, size)
                self.assertEqual(result, expected)
                self.assertEqual(values, original)
                self.assertIsInstance(result, list)
                self.assertIsNot(result, values)
                self.assertEqual(len({id(part) for part in result}), len(result))
                for index, part in enumerate(result):
                    self.assertIsInstance(part, list)
                    self.assertIsNot(part, values)
                    self.assertLessEqual(len(part), size)
                    part.append("added")
                    self.assertEqual(values, original)
                    for later in range(index + 1, len(result)):
                        self.assertEqual(result[later], expected[later])

    def test_empty_input(self):
        for size in (1, 2, 5):
            with self.subTest(size=size):
                values = []
                result = chunked(values, size)
                self.assertEqual(result, [])
                self.assertIsNot(result, values)
                result.append(["added"])
                self.assertEqual(values, [])

    def test_invalid_sizes_for_empty_and_nonempty_inputs(self):
        invalid_sizes = (True, False, 0, -1, 1.0, "2", None, [], {})
        for values in ([], [1, 2]):
            for size in invalid_sizes:
                with self.subTest(values=values, size=size):
                    original = values.copy()
                    with self.assertRaises(ValueError):
                        chunked(values, size)
                    self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
