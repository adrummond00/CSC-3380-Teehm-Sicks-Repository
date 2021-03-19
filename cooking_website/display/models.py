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

class SearchEngine(models.Model):
    __recipes = []
    __hits = []
    
    
    def __init__(self):       


        #default filter settings
        self._price = 'none'
        self._name = 'none'
        self._ingredients = 'none'

        #initialize filters with no settings/keys
        self._ingredientsFilter = (self.__recipes, [])
        self._priceFilter = (self.__recipes, 'none')
        self._nameFilter = (self.__recipes, 'none')
        

    def changePrice(self, price):
        self._price = price
        
    def changeName(self, Name):
        self._name = Name

    def addIngredients(self, ingredients):
        self._ingredients = ingredients.split(",")
        
    def __newNameFilter(self):
        self._nameFilter = NameFilter(self._name)

    def __newPriceFilter(self):
        self._priceFilter = PriceFilter(self._price)

    def __newIngredientFilter(self):
        self._ingredientsFilter = IngredientFilter(self._ingredients)
        
    def searchFilters(self):

        self.__newNameFilter()
        self.__newPriceFilter()
        self.__newIngredientFilter()

        

        file = open('DataBase.txt', 'r')
        i=-1
        for line in file:

            
            if '*' in line:
                i += 1
                self.__recipes.append(line.strip('*').strip('\n'))
                self.__hits.append(0)
                self.__hits[i] = self._nameFilter.search(line, self.__hits[i])

            if '$' in line:
                self.__hits[i] = self._priceFilter.search(line, self.__hits[i])

            if '&' in line:
                self.__hits[i] = self._ingredientsFilter.search(line, self.__hits[i])
            
            
        file.close()
        
        self.insertionSort()
        return self.__recipes

    #modified insertion sort for our purposes
    def insertionSort(self): 
  
        for i in range(1, len(self.__hits)): 
      
            key = self.__hits[i]
            ikey = self.__recipes[i]
      
            j = i-1
            while j >=0 and key > self.__hits[j] : 
                    self.__hits[j+1] = self.__hits[j]
                    self.__recipes[j+1] = self.__recipes[j]
                    j -= 1
            self.__hits[j+1] = key
            self.__recipes[j+1] = ikey
        

