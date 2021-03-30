from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import SearchToolForm, RecipeSubmissionForm, MealPlanForm, SearchEngine
import shutil
#import re
from .meal_plan import daily_plan, daily_meals


# views.py includes functions that take web requests and returns web responses


# Developed by Khanh Vu
# This function responds to "GET / HTTP/1.1" request to display the Homepage.
def Homepage(request):
    return render(request,'display/homepage.html/')

# Developed by Khanh Vu
# This function responds to both "GET /search HTTP/1.1" and "POST /search HTTP/1.1" requests, 
# if request method is POST and form is valid, it'll read price_filter, name and ingredients,
# then call SearchEngine to look up those values in the database. The top 3 relevant recipes will
# then be displayed under the search form.
# If request method is not POST, only search form is displayed.
def SearchTool(request):
    form = SearchToolForm(request.POST or None)
    f = open("display/Output.txt", "a")
    f.truncate(0)
    f.write('')
    f.close()
    
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

            # go through all recipes in the database and rank them by relevancy
            obj = SearchEngine()
            obj.changePrice(price_range)
            obj.changeName(name)
            obj.addIngredients(ingredients)
            #obj.printEverything()
            recipes = obj.searchFilters()

            all_recipe_details = []
            FindRecipeDetails(recipes)

            for i in range (0,5):
                all_recipe_details.append(FindRecipeDetailsForOneRecipe(recipes[i]))
            
            
            return render(request,'display/search_tool.html/', {
                'form': form,
                'recipes': json.dumps(all_recipe_details),
                'downloadable': 1,
            })
    
    return render(request,'display/search_tool.html/', {
        'form':form
    })


# Developed by Khanh Vu
# A function that takes one recipe name, finds it in the database and return a list of strings in this format:
# [<recipe_name>, <cost>, <ingredients>, <instructions>]
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
            if line.strip('* ').strip('\n') in recipes[i] and i < 5: #checks to see if the current line in the database matches a recipe in the list and makes sure it is only checking the top 3 results
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


# Developed by Khanh Vu
# This function responds to both "GET /submission HTTP/1.1" and "POST /search HTTP/1.1" requests, 
# if request method is POST and form is valid, it'll read cost, name and ingredients passed by the web request,
# then call RecipeSubmissionProcess to insert information to the database and tell the template to return success message.
# If request method is not POST, only search form is displayed.
def RecipeSubmission(request):
    form = RecipeSubmissionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cost = form['cost'].data
            name = form['name'].data
            ingredients = form['ingredients'].data
            direction = form['direction'].data
            RecipeSubmissionProcess(cost, name, ingredients, direction)
            return render(request,'display/recipe_submission.html/', {
                'form':form,
                'success_msg': 1,
            })
    return render(request,'display/recipe_submission.html/', {
        'form':form
    })


#developed by Jacob Dickson and Ikaika Lee
def MealPlan(request):
    form = MealPlanForm(request.POST or None)
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
                'downloadable': 1,
            })
    f = open("display/MealPlanTemplate.txt", "a")
    f.truncate(0)
    f.write("Monday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Tuesday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Wednesday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Thursday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Friday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Saturday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.write("Sunday:\n-Breakfast\n\n-Lunch\n\n-Dinner\n\n")
    f.close()
    return render(request, 'display/meal_plan.html/', {
        'form': form,
        'monBreakfast': '',
        'monLunch': '',
        'monDinner': '',
        'tueBreakfast': '',
        'tueLunch': '',
        'tueDinner': '',
        'wedBreakfast': '',
        'wedLunch': '',
        'wedDinner': '',
        'thuBreakfast': '',
        'thuLunch': '',
        'thuDinner': '',
        'friBreakfast': '',
        'friLunch': '',
        'friDinner': '',
        'satBreakfast': '',
        'satLunch': '',
        'satDinner': '',
        'sunBreakfast': '',
        'sunLunch': '',
        'sunDinner': '',
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


#developed by Jacob Dickson
#adds the meal to the correct spot in the MealPlanTemplate.txt
#name = string, name of meal
#day = string, day of the week
#meal = string, type of meal ex: Breakfast, Lunch, and Dinner
def AddToMealPlan(name, day, meal):
    comp = day + ":\n"
    compMeal = "-" + meal + "\n"
    mealPlan = open("display/MealPlanTemplate.txt", "r")
    fileContent = mealPlan.readlines()
    correctDay = False
    correctMeal = False
    
    i = 0
    while i < len(fileContent) - 1:
        if fileContent[i] == comp:
            correctDay = True
            correctMeal = False
        
        if fileContent[i] == compMeal:
            correctMeal = True

        if correctDay and correctMeal:
            fileContent[i+1] = name + "\n"
            correctDay = False
            correctMeal = False
        i += 1

    mealPlan.close()
    
    # Opens and adds additions to the Meal Plan Template and closes the file
    mealPlan = open("display/MealPlanTemplate.txt", "w")
    mealPlan.writelines(fileContent)
    mealPlan.close()


# Developed by Khanh Vu
# This function responds to "GET /help HTTP/1.1" request to display the Help page.
def Help(request):
    return render(request,'display/help.html/')


# Developed by Khanh Vu
# This function responds to "GET /download/?file_name=<file_name> HTTP/1.1" request,
# which allows user to download the file name
def GetTextFile(request):
    file_name = request.GET.get('file_name')
    with open('display/{}.txt'.format(file_name), 'r') as file:
        output = file.read()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}.txt"'.format(file_name)
    response.write(output)
    return response
