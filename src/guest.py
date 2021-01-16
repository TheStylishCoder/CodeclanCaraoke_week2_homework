class Guest:

    def __init__(self, name, money, favourite_song):
        self.name = name 
        self.money = money
        self.favourite_song = favourite_song

    def has_sufficient_funds(self, room):
        return self.money >= room.fee 