from Filter import Filter
class IngredientFilter(Filter):

    def search(self, line, hits):

        if(len(self._key) > 0):

            for ingredient in range(len(self._key)):

                if self._key[ingredient].lower() in line.lower():

                    hits += 1

        return hits
