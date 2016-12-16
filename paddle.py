import pygame
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.color = color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)



    def move(self):
        """This function makes the paddle follow the mouse"""
        xPos = pygame.mouse.get_pos()[0]
        self.rect.x = xPos

