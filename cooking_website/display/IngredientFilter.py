#by Anthony Vuong
#inherited from Filter.py
from .Filter import Filter

#the key for this class is a list of strings (ingredients)
class IngredientFilter(Filter):

    #search line for all ingredients similarities
    def search(self, line, hits):
        
        #skips search if no ingredients in list
        if(len(self._key) > 0):
            
            #iterates and checks the line for each ingredient in the list
            for ingredient in range(len(self._key)):

                if self._key[ingredient].lower() in line.lower():

                    hits += 1
                    #low weight for each ingredient, but multiple ingredients could stack fairly quickly
        return hits
        #returns weight number
    
    #deletes all ingredients
    def delKey(self):

        self._key = []

    #deletes specific ingredient
    def delIngredient(self, ingredient):

        for item in range(len(self._key)):
            if ingredient.lower() == self._key[item-1]:
                del self._key[item-1]
