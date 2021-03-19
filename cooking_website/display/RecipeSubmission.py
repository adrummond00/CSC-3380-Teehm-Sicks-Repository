from models import cost, name, ingredients, direction
class RecipeSubmission:
    otherClass = RecipeSubmissionForm()
    recipeSubmit = open("Database.txt", "a")
    recipeSubmit.write('\n* ')
    recipeSubmit.write(otherClass.name)
    recipeSubmit.write(' & ')
    recipeSubmit.write(otherClass.ingredients)
    recipeSubmit.write(" $ ")
    recipeSubmit.write(otherClass.cost)
    recipeSubmit.write(" : ")
    recipeSubmit.write(otherClass.direction)
    recipeSubmit.close()
    
