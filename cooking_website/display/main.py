class RecipeSubmission:
    recipeSubmit = open("Database.txt", "a");
    recipeSubmit.write('\n* ');
    recipeSubmit.write(name);
    recipeSubmit.write(' & ');
    recipeSubmit.write(ingredients);
    recipeSubmit.write(" $ ");
    recipeSubmit.write(price);
    recipeSubmit.write(" : ");
    recipeSubmit.write(steps);
    recipeSubmit.close();
    print(name, ingredients, price, steps);


