from .models import RecipeSubmissionForm

class RecipeSubmission:
    recipeSubmit = open("Database.txt", "a");
    recipeSubmit.write('\n* ');
    recipeSubmit.write(RecipeSubmissionForm.name);
    recipeSubmit.write('\n& ');
    recipeSubmit.write(ingredients);
    recipeSubmit.write("\n$ ");
    recipeSubmit.write(cost);
    recipeSubmit.write("\n: ");
    recipeSubmit.write(direction);
    recipeSubmit.close();
    
