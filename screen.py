import pygame, objects
from pygame.locals import *
pygame.init()

class Camera(object):
    def __init__(self, (width, height)):
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.background = pygame.Surface((width, height))
        
    def draw(self):
        for group in objects.getObjects()[:-1]:
            group.clear(self.screen, self.background)
                
        for group in objects.getObjects()[:-1]:
            group.draw(self.screen)       
            
    def Colour(self, (R, G, B)):
        # Change background colour
        self.background.fill((R, G, B))
        self.screen.blit(self.background, (0,0))
        
        
      