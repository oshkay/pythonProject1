def favoriteFood():
    print("Omlet")


class Meal:
    """Hold the food and drink used in a meal"""

    def __init__(self, food='omelet', drink='coffee'):
        self.name = 'generic meal'
        self.food = food
        self.drink = drink

    def printIt(self, prefix=''):
        """Print data"""
        print(prefix, "A fine", self.name, 'with ', self.food, 'and ', self.drink)

    def setFood(self, food):
        self.food = food

    def setDrink(self, drink):
        self.drink = drink

    def setName(self, name):
        self.name = name


class Breakfast(Meal):
    """For breakfast"""

    def __init___(self):
        Meal.__init__(self, "omeletik", 'coffee')
        self.name.setName("breakfast")


class Lunch(Meal):
    """For breakfast"""

    def __init___(self):
        Meal.__init__(self, "sandwich", 'tonic and gin')
        self.name.setName("midday meal")

    def setFood(self, food='sandwich'):
        if food != 'sandwich' and food != 'omeletik':
            raise AngryChefException
            Meal.setFood(self, food)


class Dinner(Meal):
    def __init__(self):
        Meal.__init__(self, "omeletik", 'coffee')
        self.name.setName("dinner")

    def printIt(self, prefix=''):
        """print dinner"""
        print("gourmet")

class SensitiveArtistException():
    pass

class AngryChefException(SensitiveArtistException):
    pass

