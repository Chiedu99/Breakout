#Chiedu Nduka-eze 12/16/16
#This class is for creating the ball

import pygame
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.orb = pygame.Surface((self.RADIUS, self.RADIUS))
        self.rect = self.orb.get_rect()
        self.speedx = 7
        self.speedy = 4



    def move(self):
        """This function moves the ball and makes it bounce of the walls"""
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > self.windowHeight or self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.speedx = -self.speedx

    def padCollide(self,spriteGroup):
        """This function makes the ball bounce of the paddle"""
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy


    def brickCollide(self, spriteGroup):
        """This function makes the ball bounce of bricks"""
        if pygame.sprite.spritecollide(self,spriteGroup, True):
            self.speedy = -self.speedy