from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#import json
#import requests

# homepage
def Homepage(request):
    return HttpResponse('This is homepage.')

# search tool
def SearchTool(request):
    return HttpResponse('This is search page.')

# recipe submission
def RecipeSubmission(request):
    return HttpResponse('This is recipe submission page.')

# meal plan
def MealPlan(request):
    return HttpResponse('This is meal plan page.')
