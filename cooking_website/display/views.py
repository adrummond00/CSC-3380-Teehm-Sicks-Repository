from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchToolForm, RecipeSubmissionForm

def Homepage(request):
    return render(request,'display/homepage.html/')

def SearchTool(request):
    form = SearchToolForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            price_range = form['price_filter'].data
    return render(request,'display/search_tool.html/', {'form':form})

def RecipeSubmission(request):
    form = RecipeSubmissionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cost = form['cost'].data
            name = form['name'].data
            ingredients = form['ingredients'].data
            direction = form['direction'].data
            RecipeSubmissionProcess(cost, name, ingredients, direction)
    return render(request,'display/recipe_submission.html/', {'form':form})

def MealPlan(request):
    #test = SearchEngine("hello","hello","hello")
    #print(test._price)
    return HttpResponse('This is meal plan page.')

def RecipeSubmissionProcess(cost, name, ingredients, direction):
    #form = RecipeSubmissionForm()
    recipeSubmit = open("display/DataBase.txt", "a")
    recipeSubmit.write('\n*')
    recipeSubmit.write(name)
    recipeSubmit.write('\n&')
    recipeSubmit.write(ingredients)
    recipeSubmit.write("\n$")
    recipeSubmit.write(cost)
    recipeSubmit.write("\n:")
    recipeSubmit.write(direction)
    recipeSubmit.close()
