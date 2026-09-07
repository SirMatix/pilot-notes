import io
import unittest
from contextlib import redirect_stdout

from src.pilot_notes.cli import main
from src.pilot_notes.normalize import normalize


class NormalizeTests(unittest.TestCase):
    def test_already_normalized(self):
        self.assertEqual(normalize("Hello World"), "Hello World")

    def test_whitespace_and_unicode(self):
        cases = [
            ("", ""),
            (" \t\r\n\v\f\u00a0\u2003\u202f\u3000", ""),
            ("  One\tTwo\r\nThree\vFour\fFive  ", "One Two Three Four Five"),
            (" Café\u00a0世界!\u2003A-b,\u202fÉlan\u3000", "Café 世界! A-b, Élan"),
            (" e\u0301\u200b🙂\u200d🚀 ", "e\u0301\u200b🙂\u200d🚀"),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                result = normalize(value)
                self.assertEqual(result, expected)
                self.assertEqual(normalize(result), result)

    def test_cli_prints_exactly_one_newline(self):
        for value, expected in [("", "\n"), (" \t\n", "\n"),
                                (" Café\u00a0世界!\n", "Café 世界!\n")]:
            with self.subTest(value=value):
                output = io.StringIO()
                with redirect_stdout(output):
                    main(["normalize", value])
                self.assertEqual(output.getvalue(), expected)
