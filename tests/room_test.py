import unittest
from src.room import Room 

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Booth 1")

    def test_room_has_name(self):
        self.assertEqual("Booth 1", self.room.name)

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

        