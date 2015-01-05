__author__ = 'lordobius'
import shape

class Entity:
    _shape = None
    _pos = None

    def __init__(self, shapeObject, position):
        if shapeObject or position:
            self._shape = shapeObject
            self._pos = position
        else:
            self._shape = shape.Shape(None)
            self._pos = (0, 0)

    def getPos(self):
        return self._pos

    def getShape(self):
        return self._shape

    def setShape(self, shapeObject):
        return Entity(shapeObject, self._pos)

    def setPosition(self, position):
        return Entity(self._shape, position)