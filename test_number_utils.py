import unittest

from number_utils import clamp


class ClampTests(unittest.TestCase):
    def test_integer_interval(self):
        for value, expected in ((-2, 0), (12, 10), (4, 4), (0, 0), (10, 10)):
            with self.subTest(value=value):
                self.assertEqual(clamp(value, 0, 10), expected)

    def test_float_interval(self):
        cases = ((-1.5, -1.0), (3.0, 2.5), (0.5, 0.5),
                 (-1.0, -1.0), (2.5, 2.5))
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(clamp(value, -1.0, 2.5), expected)

    def test_in_range_value_is_returned_without_coercion(self):
        for value, lower, upper in ((1.5, 0, 2), (1, 0.0, 2.0),
                                    (0.0, 0, 2), (2.0, 0, 2)):
            with self.subTest(value=value, lower=lower, upper=upper):
                self.assertIs(clamp(value, lower, upper), value)

    def test_reversed_bounds_raise_before_clamping(self):
        for value, lower, upper in ((0, 10, 2), (20, 10, 2),
                                    (5, 10, 2), (1.0, 2.5, -1.0)):
            with self.subTest(value=value, lower=lower, upper=upper):
                with self.assertRaises(ValueError):
                    clamp(value, lower, upper)

    def test_equal_bounds(self):
        for boundary, values in ((3, (2, 3, 4)), (1.5, (0.5, 1.5, 2.5))):
            for value in values:
                with self.subTest(value=value, boundary=boundary):
                    self.assertEqual(clamp(value, boundary, boundary), boundary)


if __name__ == "__main__":
    unittest.main()
