from django.urls import path

from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('search',views.SearchTool,name="SearchTool"),
    path('submission',views.RecipeSubmission,name="RecipeSubmission"),
    path('mealplan',views.MealPlan,name="MealPlan"),    
]
