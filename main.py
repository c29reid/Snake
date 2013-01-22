# Look at the README.txt for instructions on how to use this program

# This game was written by Christopher Reid

# ---Bugs---
#   - It is possible for a player to kill themselves by pressing a movement key that's allowed 
#     to move to, then immdiatley press a direction key in the opposite direction before they actually move
#     e.g If a player is moving left, pressing S then D will kill the player

# TODO
#   - Add funcion docstring comments
import screen, pygame, objects, random
from pygame.locals import *


# Resolution = 40x30 16x16 blocks = 640x480 pixels
class MainGame(object):
    def __init__(self):
        # Technical initializing
        self.name = 'Snake'
        pygame.display.set_caption(self.name)
        self.resolution = (16*40, 16*30)
        self.camera = screen.Camera(self.resolution)
        self.camera.Colour((0, 0, 0))
        self.going = True
        self.paused = False
        
        # Creating objects
        self.objects = objects.getObjects()
        self.difficulty = 1
        self.blockSize = 16
        self.clock = pygame.time.Clock()
        
    def startGame(self):
        # Creating sprite groups
        self.objects.append(pygame.sprite.Group())
        self.objects.append(pygame.sprite.Group())
        self.objects[1].add(objects.Point())
        
        self.player = objects.Snake(random.randint(0,29)*self.blockSize, # Removing the possibility of instant death
                                    random.randint(0, 29) * self.blockSize)
        self.objects.append(self.player)
        
        while self.going:
            self.clock.tick(30)
            self.run()
                
    def isOver(self):
        head = self.player.head
        
        # Checking if the player is off the screens
        if head.rect.x < 0 or head.rect.y < 0:
            return False
        if head.rect.x >= 40*16 or head.rect.y >= 30*16:
            return False
        
        # Checking if the head collided with any of the body 
        #   (the head will always be colliding with itself)
        return not len(pygame.sprite.spritecollide(head, self.objects[0], False)) > 1
    
    def run(self): 
        # Main game logic
        objects.countUp()
        self.going = self.isOver()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.going = False
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.paused = not self.paused
                
                 # Movement
                 
                 # Extra conditions are to prevent the player from running straight into itself
                if event.key == K_w or event.key == K_UP and (self.player.direction != 'd' or len(self.player.bodyList) == 1):  
                    self.player.direction = 'u'
                elif event.key == K_a or event.key == K_LEFT and (self.player.direction != 'r' or len(self.player.bodyList) == 1):
                    self.player.direction = 'l'
                elif event.key == K_s or event.key == K_DOWN and (self.player.direction != 'u' or len(self.player.bodyList) == 1):
                    self.player.direction = 'd'
                elif event.key == K_d or event.key == K_RIGHT and (self.player.direction != 'l' or len(self.player.bodyList) == 1):
                    self.player.direction = 'r'
         
        if not self.paused:        
            for group in objects.getObjects()[:-1]:
                group.update()
                
            if objects.getTime() % 4 == 0:
                objects.getObjects()[-1].update()
            
        self.camera.draw()
        pygame.display.flip()  
            
if __name__ == '__main__':
    game = MainGame()
    game.startGame()
        
        