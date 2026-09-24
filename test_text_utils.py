import unittest

from text_utils import slugify


class SlugifyTests(unittest.TestCase):
    def test_ascii_slug_examples(self):
        cases = [
            (" Hello, WORLD! ", "hello-world"),
            ("Version 2.0", "version-2-0"),
            ("A___B---C", "a-b-c"),
            ("abc123", "abc123"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_empty_and_korean_inputs(self):
        cases = [
            ("", ""),
            (" --_!? ", ""),
            ("한글", ""),
            ("A한글B", "a-b"),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    def test_non_ascii_letters_and_digits_are_separators(self):
        self.assertEqual(slugify("Aé９٢B"), "a-b")

    def test_lowercase_conversion_precedes_ascii_filtering(self):
        self.assertEqual(slugify("K"), "k")


if __name__ == "__main__":
    unittest.main()
