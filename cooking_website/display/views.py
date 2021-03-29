from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import SearchToolForm, RecipeSubmissionForm, MealPlanForm, SearchEngine
import shutil
import re
from .meal_plan import daily_plan, daily_meals
#from .SearchEngine import SearchEngine

def Homepage(request):
    return render(request,'display/homepage.html/')

def SearchTool(request):
    form = SearchToolForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            price_range = form['price_filter'].data
            name = form['name'].data
            ingredients = form['ingredients'].data

            if price_range == 'under_5': #if else statement to convert button value into integer to be compared in the price filter
                price_range = 5
            elif price_range == '5_10':
                price_range = 10
            else:
                price_range = 15

            obj = SearchEngine()
            obj.changePrice(price_range)
            obj.changeName(name)
            obj.addIngredients(ingredients)
            obj.printEverything()
            recipes = obj.searchFilters()

            all_recipe_details = []

            for i in range (0,len(recipes)):
                all_recipe_details.append(FindRecipeDetailsForOneRecipe(recipes[i]))
            
            return render(request,'display/search_tool.html/', {
                'form': form,
                'recipes': json.dumps(all_recipe_details)
            })
    return render(request,'display/search_tool.html/', {
        'form':form
    })

def FindRecipeDetailsForOneRecipe (recipe):
    with open('display/DataBase.txt') as f:
        for line in f:
            
            if recipe in line:
                ingredients = next(f).strip('& ')
                cost = next(f).strip('$ ')
                instructions = next(f).strip(': ')
                return [recipe,cost.strip('\n'),ingredients.strip('\n'),instructions.strip('\n')]

#Developed by Ikaika Lee
#Function to find the details of the returned recipes based on the user's input

def FindRecipeDetails(recipes):
    i = 0
    read = open("display/DataBase.txt", "r")
    for line in read:
        if '*' in line:
            if line.strip('* ').strip('\n') in recipes[i] and i < 3: #checks to see if the current line in the database matches a recipe in the list and makes sure it is only checking the top 3 results
                outputDetails = open('display/Output.txt', 'a')
                outputDetails.write(line.strip('* ')) #strip the key symbol off the recipe's name in the database
                outputDetails.write(next(read).strip('& ')) #strip the key symbol off the recipe's ingredients in the database
                outputDetails.write(next(read).strip('$ ')) #strip the key symbol off the recipe's price in the database
                outputDetails.write(next(read).strip(': ')) #strip the key symbol off the recipe's steps in the database
                outputDetails.write('\n')
                outputDetails.close()
                read.seek(0,0) #reposition position in database to the top
                i += 1 #incrimenting as a recipe is found
    read.close()
    #print(outputDetails)



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
            meal = form['meal'].data
            AddToMealPlan(name, day, meal)
            total = day+meal
            daily_meals[total] = name
            
    return render(request, 'display/meal_plan.html/', {
        'form': form,
        'monBreakfast': daily_meals['MondayBreakfast'],
        'monLunch': daily_meals['MondayLunch'],
        'monDinner': daily_meals['MondayDinner'],
        'tueBreakfast': daily_meals['TuesdayBreakfast'],
        'tueLunch': daily_meals['TuesdayLunch'],
        'tueDinner': daily_meals['TuesdayDinner'],
        'wedBreakfast': daily_meals['WednesdayBreakfast'],
        'wedLunch': daily_meals['WednesdayLunch'],
        'wedDinner': daily_meals['WednesdayDinner'],
        'thuBreakfast': daily_meals['ThursdayBreakfast'],
        'thuLunch': daily_meals['ThursdayLunch'],
        'thuDinner': daily_meals['ThursdayDinner'],
        'friBreakfast': daily_meals['FridayBreakfast'],
        'friLunch': daily_meals['FridayLunch'],
        'friDinner': daily_meals['FridayDinner'],
        'satBreakfast': daily_meals['SaturdayBreakfast'],
        'satLunch': daily_meals['SaturdayLunch'],
        'satDinner': daily_meals['SaturdayDinner'],
        'sunBreakfast': daily_meals['SundayBreakfast'],
        'sunLunch': daily_meals['SundayLunch'],
        'sunDinner': daily_meals['SundayDinner'],
    })
#developed by Ikaika Lee
#function adds recipe inputted by the user into the database
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

def AddToMealPlan(name, day, meal):
    comp = day + ":\n"
    compMeal = meal + ':\n'
    mealPlan = open("display/MealPlanTemplate.txt", "r")
    fileContent = mealPlan.readlines()
    i = 3
    j = 0
    k = 0
    #print(name)
    #print(allLines[0])
    for line in fileContent:
        #print(comp)
       #print(line)
        if line == comp:
            while j < 7:
                if fileContent[i+k] == compMeal:
                    fileContent[(i+k)+1] = name + '\n'
                i += 2
                j += 1
        k += 1
    mealPlan = open("display/MealPlanTemplate.txt", "w")
    mealPlan.writelines(fileContent)
    mealPlan.close()
    
    
def Help(request):
    return render(request,'display/help.html/')
