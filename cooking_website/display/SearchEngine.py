#By Anthony Vuong
#main search engine, needs no initial inputs
#returns a list sorted from most relevant recipe names to least relevant
from Filter import Filter
from PriceFilter import PriceFilter
from NameFilter import NameFilter
from IngredientFilter import IngredientFilter

class SearchEngine():
    __recipes = [] #list of recipes names
    __hits = [] #associated list with __recipes with each index containing a number denoting the correlating recipe's relevance
    
    
    def __init__(self):       


        #default filter settings
        self._price = 'none'
        self._name = 'none'
        self._ingredients = 'none'

        #initialize filters with no settings/keys
        self._ingredientsFilter = (self.__recipes, [])
        self._priceFilter = (self.__recipes, 'none')
        self._nameFilter = (self.__recipes, 'none')
        
    #changes price key
    def changePrice(self, price):
        self._price = price
    #changes Name key
    def changeName(self, Name):
        self._name = Name
    #adds ingredient to ingredients list
    def addIngredients(self, ingredients):
        self._ingredients = ingredients.split(",")
   

    #initializes the filters for searching
    def __newNameFilter(self):
        self._nameFilter = NameFilter(self._name)

    def __newPriceFilter(self):
        self._priceFilter = PriceFilter(self._price)

    def __newIngredientFilter(self):
        self._ingredientsFilter = IngredientFilter(self._ingredients)
    
    
    #Search method
    def searchFilters(self):
        
        #initializes all the filters
        self.__newNameFilter()
        self.__newPriceFilter()
        self.__newIngredientFilter()
        
        #searches through the recipe database and looks for special symbols that denote the type of information on that line
        file = open('DataBase.txt', 'r')
        
        i=-1    #keeps track of what recipe we are on
       
        for line in file:
            
            if '*' in line: #name symbol
                i += 1
                self.__recipes.append(line.strip('*').strip('\n'))
                self.__hits.append(0)
                self.__hits[i] = self._nameFilter.search(line, self.__hits[i])

            if '$' in line: #price symbol
                self.__hits[i] = self._priceFilter.search(line, self.__hits[i])

            if '&' in line: #ingredient symbol
                self.__hits[i] = self._ingredientsFilter.search(line, self.__hits[i])                  
        file.close()
        
        #sorts our list using the weight list
        self.insertionSort()
        
        return self.__recipes   #returns sorted __recipes list 

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
        
    #print stuffs
    def printEverything(self):
        print(self._nameFilter)
        print(self._priceFilter)
        print(self._ingredientsFilter)

