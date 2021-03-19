from Filter import Filter

class NameFilter(Filter):

    def search(self, line, hits):

        if(self._key != 'none'):
        
                 if self._key.lower() in line.lower():

                     hits += 100

        return hits
