import unittest
from src.room import Room 
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):

    def setUp(self):
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

        self.guest_1 = Guest("Pam Halpert", 20.00)
        self.guest_2 = Guest("Jim Halpert", 15.00)
        self.guest_3 = Guest("Michael Scott", 5.00)
        self.guest_4 = Guest("Dwight Schrute", 8.00)
        self.guest_5 = Guest("Angela Martin", 25.00)
        self.guest_6 = Guest("Oscar Martinez", 6.00)
        self.guest_7 = Guest("Kevin Malone", 10.00)
        

    def test_room_has_name(self):
        self.assertEqual("Booth 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_room_has_playlist(self):
        self.assertEqual(10, len(self.room.playlist))

    def test_room_has_entry_fee(self):
        self.assertEqual(8.00, self.room.fee)

    def test_room_occupants_starts_at_0(self):
        self.assertEqual(0, len(self.room.occupants)) 

    def test_room_waiting_list_starts_at_0(self):
        self.assertEqual(0, len(self.room.waiting_list))

    def test_add_guest_to_waiting_list(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.assertEqual(1, len(self.room.waiting_list))

    def test_remove_guest_from_waiting_list(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.remove_guest_from_waiting_list(self.guest_1)

    def test_check_in_guest_to_room(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.check_in_guest_to_room(self.guest_1)
        self.assertEqual(0, len(self.room.waiting_list))
        self.assertEqual(1, len(self.room.occupants))

    def test_check_out_guest_from_room(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.check_in_guest_to_room(self.guest_1)
        self.room.check_out_guest_from_room(self.guest_1)
        self.assertEqual(0, len(self.room.waiting_list))
        self.assertEqual(0, len(self.room.occupants))


    def test_can_add_songs_to_room_playlist(self):
        self.room.add_song_to_playlist(self.song_11)
        self.assertEqual(11, len(self.room.playlist))

    # def test_room_has_met_capacity_returns_true(self):
    #     self.room.check_in_guest_to_room(self.guest_1)
    #     self.room.check_in_guest_to_room(self.guest_2)
    #     self.room.check_in_guest_to_room(self.guest_3)
    #     self.room.check_in_guest_to_room(self.guest_4)
    #     self.assertEqual(True, self.room.room_has_met_capacity())

    # def test_room_has_met_capacity_returns_false(self):
    #     self.room.check_in_guest_to_room(self.guest_1)
    #     self.room.check_in_guest_to_room(self.guest_2)
    #     self.assertEqual(False, self.room.room_has_met_capacity())

    # def test_checking_capacity_under_capacity(self): here
    #     self.room.check_in_guest_to_room(self.guest_1)
    #     self.assertEqual(1, len(self.room.guestlist))
    #     self.assertEqual("There's still room for another guest in this booth.", self.room.checking_capacity_level())

    # def test_checking_capacity_has_been_met(self):
    #     self.room.check_in_guest_to_room(self.guest_1)
    #     self.room.check_in_guest_to_room(self.guest_2)
    #     self.room.check_in_guest_to_room(self.guest_3)
    #     self.room.check_in_guest_to_room(self.guest_4)
    #     self.assertEqual(4, len(self.room.guestlist))
    #     self.assertEqual("This booth is now full.", self.room.checking_capacity_level())

    # def test_checking_capacity_is_over_capacity(self):
    #     self.room.check_in_guest_to_room(self.guest_1)
    #     self.room.check_in_guest_to_room(self.guest_2)
    #     self.room.check_in_guest_to_room(self.guest_3)
    #     self.room.check_in_guest_to_room(self.guest_4)
    #     self.room.check_in_guest_to_room(self.guest_5)
    #     self.assertEqual(5, len(self.room.guestlist))
    #     self.assertEqual("Sorry, this booth's capacity is 4.", self.room.checking_capacity_level())
       
    def test_can_guests_move_from_waiting_list_to_room_5_guests_1_cannot_pay(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.add_guest_to_waiting_list(self.guest_2)
        self.room.add_guest_to_waiting_list(self.guest_3)
        self.room.add_guest_to_waiting_list(self.guest_4)
        self.room.add_guest_to_waiting_list(self.guest_5)
        self.room.can_allow_guests_into_room(self.room.waiting_list)
        self.room.remove_guests_from_waiting_list_to_move_to_occupants(self.room.occupants)
        self.assertEqual(4, len(self.room.occupants))
        self.assertEqual(1, len(self.room.waiting_list))
        
    

    def test_can_guests_move_from_waiting_list_to_room_4_guests_2_cannot_pay(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.add_guest_to_waiting_list(self.guest_2)
        self.room.add_guest_to_waiting_list(self.guest_3)
        self.room.add_guest_to_waiting_list(self.guest_6)
        self.room.can_allow_guests_into_room(self.room.waiting_list)
        self.room.remove_guests_from_waiting_list_to_move_to_occupants(self.room.occupants)
        self.assertEqual(2, len(self.room.occupants))
        self.assertEqual(2, len(self.room.waiting_list))
        

    def test_can_guests_move_from_waiting_list_to_room_5_guests_all_can_pay(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.add_guest_to_waiting_list(self.guest_2)
        self.room.add_guest_to_waiting_list(self.guest_4)
        self.room.add_guest_to_waiting_list(self.guest_5)
        self.room.add_guest_to_waiting_list(self.guest_7)
        self.room.can_allow_guests_into_room(self.room.waiting_list)
        self.room.remove_guests_from_waiting_list_to_move_to_occupants(self.room.occupants)
        self.assertEqual(4, len(self.room.occupants))
        self.assertEqual(1, len(self.room.waiting_list))
        
    def test_can_guests_move_from_waiting_list_to_room_4_guests_all_can_pay(self):
        self.room.add_guest_to_waiting_list(self.guest_1)
        self.room.add_guest_to_waiting_list(self.guest_2)
        self.room.add_guest_to_waiting_list(self.guest_4)
        self.room.add_guest_to_waiting_list(self.guest_7)
        self.room.can_allow_guests_into_room(self.room.waiting_list)
        self.room.remove_guests_from_waiting_list_to_move_to_occupants(self.room.occupants)
        self.assertEqual(4, len(self.room.occupants))
        self.assertEqual(0, len(self.room.waiting_list))
  

  
