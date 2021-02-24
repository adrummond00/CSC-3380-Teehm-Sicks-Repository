from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    #return HttpResponse('This is homepage.')
    return render(request,'display/homepage.html/')
def SearchTool(request):
    return HttpResponse('This is search tool.')

def RecipeSubmission(request):
    return HttpResponse('This is recipe submission page.')

def MealPlan(request):
    return HttpResponse('This is meal plan page.')
