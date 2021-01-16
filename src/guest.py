class Guest:

    def __init__(self, name, money, favourite_song):
        self.name = name 
        self.money = money
        self.favourite_song = favourite_song

    def has_sufficient_funds(self, room):
        return self.money >= room.fee 

    def cheers_for_favourite_song(self, playlist):
        for song in playlist:
            if song.title == self.favourite_song:
                return "Whoo! I love this song."
        return "Boo. They don't have my favourite song."