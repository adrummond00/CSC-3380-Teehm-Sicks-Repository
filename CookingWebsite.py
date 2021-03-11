class Filters:
    def __init__(self, n, p, l):
        self.name = n
        self.price = p
        self.otherFilter = l


class MealPlan:
    arr_mealPlan = [] * 7


class RecipeSubmission:
    def __init__(self, name, type, meat, vegetables, carbs, sauces):
        self.name = name
        self.type = type
        self.meat = meat
        self.vegetables = vegetables
        self.carbs = carbs
        self.sauces = sauces
    recipeSubmit = open("RecipeFile.txt", "a")
    recipeSubmit.write('* ', name, '& ')
    recipeSubmit.close()


class ListRecipes:
    recipeList = open("RecipeFile.txt", "r")


