__author__ = 'lordobius'
import pygame
from Game import engine
from Game import shape
from Game import world

from threading import Thread
from time import sleep

le_monde = world.World(None, "Le_Monde_de_Jean_Claude")

le_jeu = engine.GameEngine(False, (700,500), 60, "Yolo")

def lel():
    x = 0
    print "test"
    while(x is not 30):
        print "lol"
        x += 1
        sleep(1)


if __name__ == "__main__":
    threadTest = Thread(target = lel())
    thread = Thread(target = le_jeu.start())
    thread.start()
    threadTest.start()
    threadTest.join()
    thread.join()