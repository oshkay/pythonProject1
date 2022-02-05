class Omlet:
    """This class creates an omlet object
    get_kind()
    """

    def __init__(self, recipes,  kind="cheese"):
        self.recipes = recipes
        self.set_kind(kind)

    def __ingredients__(self):
        return self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        possible_ing = self.__known_kinds(kind)
        if not possible_ing:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ing

    def set_new_kind(self, name, ings):
        self.recipes.create(name, ings)
        self.set_kind(name)
        return

    def __known_kinds(self, kind):
        return self.recipes.get(kind)

    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self)

    def mix(self, printed = True):
        if printed:
            for ing in self.from_fridge.keys():
                print("Mixing %d %s for the %s omlet " % (self.from_fridge[ing], ing, self.kind))
        self.mixed = True

    def make(self):
        if self.mixed:
            print("cooking the %s omelet!" % self.kind)
            self.cooked = True

    def test(self):
        if self.kind:
            return True
        else:
            return False
    def quick_cook(self, kind, quantity, fridge):
        self.set_kind(kind)
        self.get_ingredients(fridge)
        self.mix(False)
        self.make()
        pass