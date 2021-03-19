from Filter import Filter

class PriceFilter(Filter):

     def search(self, line, hits):

        if(self._key != 'none'):
        

          if int(self._key.strip('$')) <= int(line.strip('$')):

               hits += 10

               
        return hits
