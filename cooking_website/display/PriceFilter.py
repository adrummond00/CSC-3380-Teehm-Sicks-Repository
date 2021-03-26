#By Anthony Vuong
#inherited from Filter.py
from .Filter import Filter

class PriceFilter(Filter):

     #compares the price given (key) to the price found in the line given
     def search(self, line, hits):

        if(self._key != 'none'):
        

          if int(self._key) >= int(line.strip('$')):

               hits += 10
               #medium weight
               
        return hits
          #returns weight number
