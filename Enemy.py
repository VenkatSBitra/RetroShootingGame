import pygame
import random


class Enemy(object):
    walkRight = [pygame.image.load(r'R1E.png'), pygame.image.load(r'R2E.png'), pygame.image.load(r'R3E.png'), pygame.image.load(r'R4E.png'), pygame.image.load(r'R5E.png'), pygame.image.load(r'R6E.png'), pygame.image.load(r'R7E.png'), pygame.image.load(r'R8E.png'), pygame.image.load(r'R9E.png'), pygame.image.load(r'R10E.png'), pygame.image.load(r'R11E.png')]
    walkLeft = [pygame.image.load(r'L1E.png'), pygame.image.load(r'L2E.png'), pygame.image.load(r'L3E.png'), pygame.image.load(r'L4E.png'), pygame.image.load(r'L5E.png'), pygame.image.load(r'L6E.png'), pygame.image.load(r'L7E.png'), pygame.image.load(r'L8E.png'), pygame.image.load(r'L9E.png'), pygame.image.load(r'L10E.png'), pygame.image.load(r'L11E.png')]


    def __init__(self, y, width, height):
        self.x = random.randint(0, 1) * 788
        self.y = y
        self.width = width
        self.height = height
         
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, 50, 65)
        self.health = 10
        self.visible = True

    def draw(self, gameDisplay, man):
        self.move(man)
        if self.visible == True:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                gameDisplay.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                gameDisplay.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            if self.vel > 0:
                self.hitbox = (self.x + 10, self.y, 40, 65)
            else:
                self.hitbox = (self.x + 20, self.y, 40, 65)

            pygame.draw.rect(gameDisplay, (255,0,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(gameDisplay, (0,128,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 2)
        else:
            self.visible = True
            self.health = 10
            self.x = random.randint(0, 1) * 788
            
            pygame.draw.rect(gameDisplay, (255,0,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(gameDisplay, (0,128,0), (self.hitbox[0] - 5, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.draw(gameDisplay, man)

        

    def move(self, man):
        
        if man.x_player - self.x > 0:
            self.vel = abs(self.vel)
            self.x += self.vel
        else:
            self.vel = abs(self.vel) * -1
            self.x += self.vel
        
        

     #   if self.vel > 0:
     #      if self.x + self.vel < self.path[1]:
     #         self.x += self.vel
     #    else:
     #       self.vel = self.vel * -1
     #      self.walkCount = 0
     # else:
     #    if self.x - self.vel > self.path[0]:
     #        self.x += self.vel
     #   else:
     #      self.vel = self.vel * -1
     #     self.walkCount = 0  
        
        

    def hit(self):
         #print("KILL")
         if self.health > 0:
             self.health -= 1
         else:
             self.visible = False
             


