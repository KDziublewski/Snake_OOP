import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

display_width = 800
display_height = 600
# creates the display window, the arg for set_mode() is a tuple,
# could be a list I think tho
gameDisplay = pygame.display.set_mode((display_width, display_height))
# window name
pygame.display.set_caption('Slither')


clock = pygame.time.Clock()

block_size = 20

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, yellow, [XnY[0], XnY[1], block_size, block_size])
# function for printing msg to screen


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2 - screen_text.get_width() / 2, display_height / 2 - screen_text.get_height() / 2])
# main game loop, event handling


def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 3
    FPS = 10

    randAppleX = round(random.randrange(0, display_width-block_size))  # /10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height-block_size))  # /10.0) * 10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0

        if lead_x + block_size > display_width or lead_x < 0 or lead_y + block_size > display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)
        appleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        pygame.display.update()

        if lead_x >= randAppleX - block_size and lead_y >= randAppleY - block_size and lead_x < randAppleX + appleThickness and lead_y < randAppleY + appleThickness:
            randAppleX = round(random.randrange(0, display_width-block_size))  # /10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height-block_size))  # /10.0) * 10.0
            snakeLength += 1
            FPS += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
