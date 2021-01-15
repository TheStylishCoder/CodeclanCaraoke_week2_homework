import unittest
from src.room import Room 
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Booth 1", 4)
        self.guest = Guest("Pam Halpert")
        self.song = Song("Love Shack", "The B-52's")

    def test_room_has_name(self):
        self.assertEqual("Booth 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_guestlist_starts_at_0(self):
        self.assertEqual(0, len(self.room.guestlist))

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room.guestlist))

    def test_check_out_guest_from_room(self):
        self.room.check_in_guest_to_room(self.guest)
        self.room.check_out_guest_from_room(self.guest)
        self.assertEqual(0, len(self.room.guestlist))

    def test_can_add_songs_to_room_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.assertEqual(1, len(self.room.playlist))

    def test_room_has_met_capacity_returns_true(self):
        self.room.check_in_guest_to_room(self.guest)
        self.room.check_in_guest_to_room(self.guest)
        self.room.check_in_guest_to_room(self.guest)
        self.room.check_in_guest_to_room(self.guest)
        self.assertEqual(True, self.room.room_has_met_capacity())

    def test_room_has_met_capacity_returns_false(self):
        self.room.check_in_guest_to_room(self.guest)
        self.room.check_in_guest_to_room(self.guest)
        self.assertEqual(False, self.room.room_has_met_capacity())