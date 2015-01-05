__author__ = 'lordobius'

#The World is build like this:
#     World: [ (entity), (entity) ]
#The content of each entity: see the Entity Object


class World:
    _content = None
    _worldName = None
    _databaseConnection = None

    def __init__(self, newContent, worldName):
        if newContent is not None and type(newContent) is list:
            self._content = newContent
        else:
            self._content = dict()

        if worldName is not None and type(worldName) is str:
            self._worldName = worldName
            #self.databaseConnection = sqlite3.connect(worldName)

    def getContent(self):
        return self._content

    def setContent(self, key, value):
        self._content[key] = value
        return self._content

    def getElement(self, key):
        return self._content[key]

    def delElement(self, key):
        del self._content[key]
        return self._content