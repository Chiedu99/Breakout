import pygame
import paddle
import brick
import ball
from pygame.locals import *
import sys

def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    BRICK_HEIGHT = 8
    PWIDTH = 60
    PHEIGHT = 10

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


    pygame.init()
    mainSurface = pygame.display.set_mode((400, 600), 0, 32)

    mainSurface.fill(WHITE)

    listColors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]

    xPos = BRICK_SEP
    yPos = BRICK_Y_OFFSET
  # This loop creates a brick, places them, and changes the color for all 5 rows
    brickGroup = pygame.sprite.Group()
    for color in listColors:
        for x in range (BRICKS_PER_ROW):
            pie = brick.Brick(BRICK_WIDTH, color)
            pie.rect.x = xPos
            pie.rect.y = yPos
            brickGroup.add(pie)
            mainSurface.blit(pie.block, pie.rect)
            xPos += BRICK_SEP + BRICK_WIDTH
        yPos += BRICK_HEIGHT + BRICK_SEP
        xPos = BRICK_SEP

    # This creates the paddle and puts it into a sprite group
    pie2 = paddle.Paddle(BLACK)
    pie2.rect.x = APPLICATION_WIDTH / 2
    pie2.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(pie2.image, pie2.rect)
    paddleGroup = pygame.sprite.Group()

    # This creates the ball and puts it into a sprite group
    pie3 = ball.Ball(BLACK,APPLICATION_WIDTH, APPLICATION_HEIGHT)
    pie3.rect.x = APPLICATION_WIDTH / 2
    pie3.rect.y = APPLICATION_HEIGHT / 2
    mainSurface.blit(pie3.orb, pie3.rect)
    paddleGroup.add(pie2)

    # This creates the "you lose!" statement when you die 3 times
    myFont = pygame.font.SysFont ("Helvetica", 24)
    Label = myFont.render("YOU LOSE!",1, RED)



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(WHITE)
        for pie in brickGroup:
            # redraws all the bricks on he screen
            mainSurface.blit(pie.block, pie.rect)
        # moves the paddle
        pie2.move()
        mainSurface.blit(pie2.image, pie2.rect)
        pie3.move()
        if pie3.rect.bottom > APPLICATION_HEIGHT:
            # makes the user lose when they hit the bottom 3 times
            NUM_TURNS -= 1
            pie3.rect.x = APPLICATION_WIDTH / 2
            pie3.rect.y = APPLICATION_HEIGHT / 2
            pygame.time.wait(1000)
        mainSurface.blit(pie3.orb, pie3.rect)
        if NUM_TURNS == 0:
            # displays the losing statement
            mainSurface.fill(WHITE)
            mainSurface.blit(Label,(200,275))
            pygame.display.update()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()



        pie3.padCollide(paddleGroup)
        pie3.brickCollide(brickGroup)




        pygame.display.update()

main()
