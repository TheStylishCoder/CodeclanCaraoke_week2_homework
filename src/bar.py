class Bar:

    def __init__(self, name, till):
        self.name = name
        self.till = till 
        # self.drinks = drinks

    def add_money_to_till(self, amount):
        self.till += amount