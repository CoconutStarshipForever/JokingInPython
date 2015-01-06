__author__ = 'lordobius'
from Game import engine
from Game import shape
from Game import world

from threading import Thread
from time import sleep

le_monde = world.World(None, "Le_Monde_de_Jean_Claude")

le_jeu = engine.GameEngine(False, (700,500), 60, "Yolo")

class myThread (Thread):
    def __init__(self, threadID, name, counter, message):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.message = message
    def run(self):
        print("Starting " + self.name)
        lel(self.counter, self.message)
        print("Exiting " + self.name)

class engineMainThread (Thread):
    def __init__(self, threadID, name, gameEngine):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.engine = gameEngine
    def run(self):
        print("Starting " + self.name)
        self.engine.start()
        print("Exiting " + self.name)

def lel(duration, message):
    x = 0
    print("Starting : " + message)
    while(x is not duration):
        print(message)
        x += 1
        sleep(1)


if __name__ == "__main__":
    threadTest = myThread(1, "Test 1", 5, "This is test 1")
    threadTest2 = myThread(2, "Test 2", 5, "This is test 2")
    threadGameEngine = engineMainThread(3, "The current Game Engine", le_jeu)

    threadTest2.start()
    threadTest.start()
    threadGameEngine.start()