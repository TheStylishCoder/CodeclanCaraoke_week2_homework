class Room:

    def __init__(self, name, capacity, playlist, fee): 
        self.name = name
        self.capacity = capacity
        self.playlist = playlist 
        self.fee = fee
        self.occupants = []
        self.waiting_list = []
        

    def add_guest_to_waiting_list(self, guest):
        self.waiting_list.append(guest)

    def remove_guest_from_waiting_list(self, guest):
        self.waiting_list.remove(guest)

    def check_in_guest_to_room(self, guest):
        self.remove_guest_from_waiting_list(guest) 
        self.occupants.append(guest)

    def check_out_guest_from_room(self, guest):
        self.occupants.remove(guest) 

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
       

    # def room_has_met_capacity(self):
    #     return len(self.guestlist) >= self.capacity
           
    
    # def checking_capacity_level(self):
    #     if len(self.guestlist) == self.capacity:
    #         return "This booth is now full." 
    #     elif len(self.guestlist) > self.capacity:
    #         return "Sorry, this booth's capacity is " + str(self.capacity) + "."
    #     elif len(self.guestlist) < self.capacity:
    #         return "There's still room for another guest in this booth."   


    def can_allow_guests_into_room(self, waiting_list):
        for guest in waiting_list:
            if (len(self.occupants) < self.capacity) and (guest.money >= self.fee):
                self.occupants.append(guest)
        
       
    def remove_guests_from_waiting_list_to_move_to_occupants(self, occupants):
        for guest in occupants:
            if guest in self.waiting_list:
                self.waiting_list.remove(guest)
               