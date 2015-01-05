__author__ = 'lordobius'
import pygame
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SuperBrutalStickGameTest")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
print "he has finish"