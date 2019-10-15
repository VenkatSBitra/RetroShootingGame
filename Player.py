import pygame
import random

global bullets
bullets = []

class Player(object):
    walkRight = [pygame.image.load(r'R1.png'), pygame.image.load(r'R2.png'), pygame.image.load(r'R3.png'), pygame.image.load(r'R4.png'), pygame.image.load(r'R5.png'), pygame.image.load(r'R6.png'), pygame.image.load(r'R7.png'), pygame.image.load(r'R8.png'), pygame.image.load(r'R9.png')]
    walkLeft = [pygame.image.load(r'L1.png'), pygame.image.load(r'L2.png'), pygame.image.load(r'L3.png'), pygame.image.load(r'L4.png'), pygame.image.load(r'L5.png'), pygame.image.load(r'L6.png'), pygame.image.load(r'L7.png'), pygame.image.load(r'L8.png'), pygame.image.load(r'L9.png')]
    standing = pygame.image.load(r'standing.png')

    def __init__(self,x,y,width,height):
        self.x_player = x
        self.y_player = y
        self.width = width
        self.height = height
        self.vel = 9
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.alive = True
        self.health = 500
        self.hitbox = (self.x_player + 17, self.y_player + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x_player,self.y_player))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x_player,self.y_player))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x_player, self.y_player))
            else:
                win.blit(self.walkLeft[0], (self.x_player, self.y_player))
        self.hitbox = (self.x_player + 17, self.y_player + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        if self.health > 0:
             self.health -= 1
        else:
             self.alive = False
