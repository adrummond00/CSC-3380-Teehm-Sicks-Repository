#By Anthony Vuong
#Inherited from Filter.py
from Filter import Filter

class NameFilter(Filter):

    #filters through a single line for a name/key
    def search(self, line, hits):

        if(self._key != 'none'):
        
                 if self._key.lower() in line.lower():

                     hits += 100
                    #Name is considered high relevance in a search engine so a large amount of 'weight' is given to it

        return hits
        #returns the weight number
