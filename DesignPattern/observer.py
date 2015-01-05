__author__ = 'lordobius'

class Observer:

    def __init__(self):
        return ""


class Subject:
    _listOfObservable = None
    def __init__(self, listOfObservable):
        self._listOfObservable = listOfObservable

    def registerObserver(self, observer):
        return Subject(self._listOfObservable.add(observer))

    def removeObserver(self, observer):
        return Subject(self._listOfObservable.remove(observer))

    def notifyObserver(self):
        for observer in self._listOfObservable:
            observer.update()