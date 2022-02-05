class Recipe:
    """
    get(recipe_name)
    create(recipe_name, ingredients)
    """
    def __init__(self):
        self.rs = {"cheese": {"eggs": 2, "milk": 1, "cheese": 1},
                   "cherry": {"cherry": 5, "eggs": 3}}

    def create(self, name, ingrs):
        self.rs[name] = ingrs

    def get(self, rc_name):
        return self.rs[rc_name]