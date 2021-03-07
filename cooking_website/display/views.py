from django.shortcuts import render
from django.http import HttpResponse
from .models import SearchToolForm

def Homepage(request):
    #return HttpResponse('This is homepage.')
    return render(request,'display/homepage.html/')
def SearchTool(request):
    #return HttpResponse('This is search tool.')
    form = SearchToolForm()
    return render(request,'display/search.html/', {'form':form})
def RecipeSubmission(request):
    return HttpResponse('This is recipe submission page.')

def MealPlan(request):
    return HttpResponse('This is meal plan page.')
