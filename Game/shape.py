__author__ = 'lordobius'

class Shape:
    theShape = None

    def __init__(self, newShape):
        if newShape is not None and type(newShape) is list:
            self.theShape = newShape
        else:
            self.theShape = list()

    def getShape(self):
        return self.theShape