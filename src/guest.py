class Guest:

    def __init__(self, name, money):
        self.name = name 
        self.money = money

    def has_sufficient_funds(self, room):
        return self.money >= room.fee 