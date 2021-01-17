import unittest
from src.bar import Bar 
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
        # drinks = [
        #     {"name": "Cosmopolitan",
        #     "price": 3.50
        #     },
        #     {"name": "French Martini",
        #     "price": 4.00
        #     },
        #     {"name": "Long Island Ice Tea",
        #     "price": 6.00
        #     },
        #     {"name": "Mojito",
        #     "price": 5.50
        #     },
        #     {"name": "Pina Colada",
        #     "price": 3.50
        #     }
        # ]
        self.bar = Bar("Caraoke Club", 500.00)
        
        self.song_1 = Song("Dancing Queen", "ABBA") 
        self.song_2 = Song("I'm Still Standing", "Elton John")
        self.song_3 = Song("9 to 5", "Dolly Parton")
        self.song_4 = Song("Crazy In Love", "Beyonce & JAY-Z")
        self.song_5 = Song("Heart Of Glass", "Blondie")
        self.song_6 = Song("Dilemma", "Nelly & Kelly Rowland")
        self.song_7 = Song("All The Small Things", "blink-182")
        self.song_8 = Song("Disco 2000", "Pulp")
        self.song_9 = Song("Don't Go Breaking My Heart", "Elton John & Kiki Dee")
        self.song_10 = Song("You Spin Me Round", "Dead Or Alive")
        self.song_11 = Song("Love Shack", "The B-52's")

        playlist = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6, self.song_7, self.song_8, self.song_9, self.song_10]
       

        self.guest = Guest("Pam Halpert", 20.00, "Don't Go Breaking My Heart")
        self.room = Room("Booth 1", 4, playlist, 8.00)
        

    def test_bar_has_name(self):
        self.assertEqual("Caraoke Club", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(500.00, self.bar.till)

    def test_bar_can_add_money_to_till(self):
        self.guest.pays(self.room)
        self.bar.add_money_to_till(self.room.fee)
        self.assertEqual(508.00, self.bar.till)
        self.assertEqual(12.00, self.guest.money)

    


    


    