import unittest
from src.bar import Bar 

class TestBar(unittest.TestCase):

    def setUp(self):
        drinks = [
            {"name": "Cosmopolitan",
            "price": 3.50
            },
            {"name": "French Martini",
            "price": 4.00
            },
            {"name": "Long Island Ice Tea",
            "price": 6.00
            },
            {"name": "Mojito",
            "price": 5.50
            },
            {"name": "Pina Colada",
            "price": 3.50
            }
        ]
        self.bar = Bar("Caraoke Club", 500.00, drinks)
        

    def test_bar_has_name(self):
        self.assertEqual("Caraoke Club", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(500.00, self.bar.till)


    


    