class Room:

    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.guestlist = []


    def check_in_guest_to_room(self, guest):
        self.guestlist.append(guest)
