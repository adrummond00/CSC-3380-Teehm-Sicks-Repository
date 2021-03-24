#base class for the filters
#by Anthony Vuong
class Filter:

    def __init__(self, key):

        self._key = key
        #key is the keyword being used to search

    def showKey(self):
        print(self._key)
