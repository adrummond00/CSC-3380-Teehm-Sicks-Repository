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
            print(cost)
    return render(request,'display/recipe_submission.html/', {'form':form})

def MealPlan(request):
    return HttpResponse('This is meal plan page.')
