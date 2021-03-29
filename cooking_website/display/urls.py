from django.urls import path
from django.conf.urls import url

#urls.py includes all URL patterns
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('search',views.SearchTool,name="SearchTool"),
    path('submission',views.RecipeSubmission,name="RecipeSubmission"),
    path('mealplan',views.MealPlan,name="MealPlan"),    
    path('help',views.Help,name="Help"),

    url(r'^download/$', views.GetTextFile, name='download'),
]
