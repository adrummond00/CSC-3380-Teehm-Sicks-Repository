from django.db import models
from django import forms

price_range = (
    ('under_5','Under $5'),
    ('5_10','$5-$10'),
    ('10-15','$10-$15'),
)
class SearchToolForm (forms.Form):
    price_filter = forms.CharField(widget=forms.Select(choices=price_range))
    name = forms.CharField(label="Name")
    ingredients = forms.CharField(label="Ingredients",widget=forms.Textarea())
class RecipeSubmissionForm (forms.Form):
    cost = forms.CharField(widget=forms.Select(choices=price_range))
    name = forms.CharField(label="Name")
    ingredients = forms.CharField(label="Ingredients",widget=forms.Textarea())
    direction = forms.CharField(label="Direction",widget=forms.Textarea())
    recipeSubmit = open("DataBase.txt", "a");
    recipeSubmit.write('\n* ');
    recipeSubmit.write(name);
    recipeSubmit.write('\n& ');
    recipeSubmit.write(ingredients);
    recipeSubmit.write("\n$ ");
    recipeSubmit.write(cost);
    recipeSubmit.write("\n: ");
    recipeSubmit.write(direction);
    recipeSubmit.close();
