import unittest
from src.pilot_notes.normalize import normalize


class NormalizeTests(unittest.TestCase):
    def test_already_normalized(self):
        self.assertEqual(normalize("Hello World"), "Hello World")
