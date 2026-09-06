import io
import unittest
from contextlib import redirect_stdout
from src.pilot_notes.normalize import normalize
from src.pilot_notes.cli import main


class ContractTests(unittest.TestCase):
    def test_normalization(self):
        cases = [("  Hello   World ", "Hello World"), ("", ""),
                 (" \t\n", ""), ("One\tTwo\nThree", "One Two Three"),
                 (" café\u00a0世界! ", "café 世界!"), ("A-b, C!", "A-b, C!")]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(normalize(value), expected)
                self.assertEqual(normalize(normalize(value)), expected)

    def test_cli(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main(["normalize", "  Hello   World "])
        self.assertEqual(output.getvalue(), "Hello World\n")
