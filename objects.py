import pygame, screen, random
from pygame.locals import *

obj = [] # 0 = Snake Parts
         # 1 = Points
         # 2 = Snake
         
time = [0] # To make time global and be accessible by different modules

def countUp():
    time[0] += 1
    
def getTime():
    return time[0]

def getObjects():
    return obj

class Snake(object):
    def __init__(self, x, y):
        self.body = obj[0]
        self.direction = 'r' # l = left; r = right; u = Up; d = Down
        self.head = Body(x, y)
        self.body.add(self.head)
        self.newBody = None
        self.bodyList = [self.head] # The group doesn't keep the body in order
        
    def move(self): 
        # Move the snake around the screen
        sprites = self.bodyList
        for i in range(1, len(sprites))[::-1]:
            sprites[i].moveTo(sprites[i-1])
        
        if self.direction == 'l':
            self.head.move(-16, 0)
        elif self.direction == 'r':
            self.head.move(16, 0)
        elif self.direction == 'u':
            self.head.move(0, -16)
        else:
            self.head.move(0, 16)   
            
        if self.newBody != None:
            self.bodyList.append(self.newBody)
            self.body.add(self.newBody)
            self.newBody = None        
            
    def update(self):
        # Ate a point
        if len(pygame.sprite.spritecollide(self.head, obj[1], True)) > 0:
            sprites = self.body.sprites()
            self.newBody = Body(sprites[-1].rect.x, sprites[-1].rect.y)
            obj[1].add(Point())
        self.move()
        
        
class Body(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
    
    def moveTo(self, body):
        self.rect = body.rect.copy()
        
    def move(self, x, y):
        self.rect.move_ip(x, y)
        
        
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 255, 0)) # Green
        self.rect = self.image.get_rect()
        self.spawn()
    
    def spawn(self):
        self.rect.move_ip(random.randint(0, 39)*16, 
                          random.randint(0, 29)*16)
        