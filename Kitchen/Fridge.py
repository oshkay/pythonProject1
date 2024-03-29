
class Fridge:
    def __init__(self, items=None):
        if items is None:
            items = {}
        if not isinstance(items, dict):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
        self.items = items

    def __add_multi(self, food_name, quantity):
        if food_name in self.items.keys():
            pass
        else:
            self.items[food_name] = 0
        self.items[food_name] += quantity

    def add_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError("add_one requires a string but given a %s" % type(food_name))
        else:
            self.__add_multi(food_name, 1)
        return True

    def add_many(self, food_dict):
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dictionary? got a %ds" % type(food_dict))
        else:
            for item in food_dict.keys():
                self.__add_multi(item, food_dict[item])
        return

    def has(self, food_name, q=1):
        return self.has_various({food_name: q})

    def has_various(self, foods):
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False

    def __get_multi(self, food_name, q):
        try:
            if not self.has(food_name, q):
                return False
            self.items[food_name] = self.items[food_name] - q
        except KeyError:
            return False
        return q

    def get_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError(" get_one require string")
        else:
            result = self.__get_multi(food_name, 1)
        return result

    def get_many(self, food_dict):
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed

    def get_ingredients(self, food):
        try:
            ing = food.__ingredients__()
            ingredients = self.get_many(ing)
        except AttributeError:
            return False
        if ingredients:
            return ingredients