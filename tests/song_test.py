import unittest
from src.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Love Shack", "The B-52's")

    def test_song_has_title(self):
        self.assertEqual("Love Shack", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("The B-52's", self.song.artist)