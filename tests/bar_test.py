import unittest
from src.bar import Bar 

class TestBar(unittest.TestCase):

    def setUp(self):
        drinks = {}
        self.bar = Bar("Caraoke Club", 500.00, drinks)
        

    def test_bar_has_name(self):
        self.assertEqual("Caraoke Club", self.bar.name)