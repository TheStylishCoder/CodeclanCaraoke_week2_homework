import unittest
from src.room import Room 
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Booth 1")
        self.guest = Guest("Pam Halpert")

    def test_room_has_name(self):
        self.assertEqual("Booth 1", self.room.name)

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_guestlist_starts_at_0(self):
        self.assertEqual(0, len(self.room.guestlist))

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room.guestlist))