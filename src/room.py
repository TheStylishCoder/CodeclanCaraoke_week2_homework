class Room:

    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.guestlist = []


    def check_in_guest_to_room(self, guest):
        self.guestlist.append(guest)

    def check_out_guest_from_room(self, guest):
        self.guestlist.remove(guest) 

    def add_song_to_playlist(self, song):
        self.playlist.append(song)
