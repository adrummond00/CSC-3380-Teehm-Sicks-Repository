from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchToolForm, RecipeSubmissionForm, MealPlanForm
import shutil
import re

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
    form = MealPlanForm(request.POST or None)
    #test = SearchEngine("hello","hello","hello")
    #print(test._price)
    if request.method == 'POST':
        if form.is_valid():
            name = form['name'].data
            day = form['day'].data
            AddToMealPlan(name, day)

    return render(request, 'display/meal_plan.html/', {'form':form})

def RecipeSubmissionProcess(cost, name, ingredients, direction):
    #form = RecipeSubmissionForm()
    recipeSubmit = open("display/DataBase.txt", "a")
    recipeSubmit.write('\n* ')
    recipeSubmit.write(name)
    recipeSubmit.write('\n& ')
    recipeSubmit.write(ingredients)
    recipeSubmit.write("\n$ ")
    recipeSubmit.write(cost)
    recipeSubmit.write("\n: ")
    recipeSubmit.write(direction)
    recipeSubmit.close()

def AddToMealPlan(name, day):
    comp = day + ":\n"
    i = 0
    mealPlan = open("display/MealPlanTemplate.txt", "r")
    allLines = mealPlan.readlines()
    size = len(allLines)
    #print(name)
    #print(allLines[0])
    while i < size-1:
        line = allLines[i]
        #print(comp)
       #print(line)
        if line == comp:
            
            allLines[i+1] = name + "\n"
        i += 1
    mealPlan.close()
    #print(allLines)
    mealPlan = open("display/MealPlanTemplate.txt", "w")
    mealPlan.writelines(allLines)
    mealPlan.close()
    