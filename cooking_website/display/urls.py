from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('search',views.SearchTool,name="SearchTool"),
    path('submission',views.RecipeSubmission,name="RecipeSubmission"),
    path('mealplan',views.MealPlan,name="MealPlan"),    
    path('help',views.Help,name="Help"),

    #path('download',views.GetTextFile,name="download"),
    url(r'^download/$', views.GetTextFile, name='download'),
]
