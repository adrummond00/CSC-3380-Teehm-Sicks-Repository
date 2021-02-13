from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.Homepage),
    path('search', views.SearchTool),
    path('submission', views.RecipeSubmission),
    path('mealplan', views.MealPlan),

]