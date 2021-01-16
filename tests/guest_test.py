import unittest
from src.guest import Guest 
from src.room import Room
from src.song import Song 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Pam Halpert", 20.00, "Don't Go Breaking My Heart")
        
        
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
       
        self.room = Room("Booth 1", 4, playlist, 8.00)

    def test_guest_has_name(self):
        self.assertEqual("Pam Halpert", self.guest.name, "Don't Go Breaking My Heart")

    def test_guest_has_money(self):
        self.assertEqual(20.00, self.guest.money)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Don't Go Breaking My Heart", self.guest.favourite_song)

    def test_guest_cheers_for_favourite_song_match_true(self):
        self.assertEqual("Whoo! I love this song.", self.guest.cheers_for_favourite_song(self.room.playlist))

    def test_guest_cheers_for_favourite_song_match_false(self):
        guest_4 = Guest("Dwight Schrute", 8.00, "We Didn't Start The Fire")
        self.assertEqual("Boo. They don't have my favourite song.", guest_4.cheers_for_favourite_song(self.room.playlist))

    def test_guest_has_sufficient_funds_for_entry_returns_true(self):
        self.assertEqual(True, self.guest.has_sufficient_funds(self.room))

    def test_guest_has_sufficient_funds_for_entry_returns_false(self):
        guest_3 = Guest("Michael Scott", 5.00, "Love Shack")
        self.assertEqual(False, guest_3.has_sufficient_funds(self.room))
