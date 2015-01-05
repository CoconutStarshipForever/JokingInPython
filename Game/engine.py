__author__ = 'lordobius'
import pygame
import colors
import world

class GameEngine:
    _fullscreen = None
    _resolution = None
    _framerate = None
    _screen = None
    _clock = None
    _gameIsClose = None

    # What he should see

    _gameContent = None

    #
    # I Have no idea if this is usefull
    #
    _thePyGameModule = None


    def __init__(self, fullscreen, resolution, framerate, theStupidName):
        self._fullscreen = fullscreen
        self._resolution = resolution
        self._framerate = framerate
        self._thePyGameModule = pygame.init()
        self._screen = pygame.display.set_mode(resolution)
        self._clock = pygame.time.Clock()
        pygame.display.set_caption(theStupidName)
        self._gameContent = world.World(None, None)
        self._gameIsClose = False

    def setWorld(self, newWorld, worldName):
        self._gameContent = world.World(newWorld, worldName)


    def start(self):
        while not self._gameIsClose:
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     self._gameIsClose = True

            self._screen.fill(colors.WHITE)
            pygame.display.flip()
            self._clock.tick(self._framerate)
        pygame.quit()
        print "he has finish"
