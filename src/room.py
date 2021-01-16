class Room:

    def __init__(self, name, capacity, playlist, fee): 
        self.name = name
        self.capacity = capacity
        self.playlist = playlist 
        self.fee = fee
        self.guestlist = []
        


    def check_in_guest_to_room(self, guest):
        self.guestlist.append(guest)

    def check_out_guest_from_room(self, guest):
        self.guestlist.remove(guest) 

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
       

    # def room_has_met_capacity(self):
    #     return len(self.guestlist) >= self.capacity
           
    
    def checking_capacity_level(self):
        if len(self.guestlist) == self.capacity:
            return "This booth is now full." 
        elif len(self.guestlist) > self.capacity:
            return "Sorry, this booth's capacity is " + str(self.capacity) + "."
        elif len(self.guestlist) < self.capacity:
            return "There's still room for another guest in this booth."   