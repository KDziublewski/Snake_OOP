import pygame
import random
pygame.init()

class Text:
    def __init__(self, msg, color, font, font_size):
        self.msg = msg
        self.color = color
        self.font = pygame.font.SysFont(font, font_size)

    def message_to_screen(self):
        self.screenText = self.font.render(self.msg, True, self.color)
        gameDisplay.blit(self.screenText, [displayWidth / 2 - self.screenText.get_width() / 2, displayHeight / 2 - self.screenText.get_height() / 2])


class Snake:
    def __init__(self, lead_x, lead_y, lead_x_change, lead_y_change, snakeLength):
        self.lead_x = lead_x
        self.lead_y = lead_y
        self.lead_x_change = lead_x_change
        self.lead_y_change = lead_y_change
        self.snakeLength = snakeLength

    def snake_move(self, snakeList, snakeHead):
        self.snakeList = snakeList
        self.snakeHead = snakeHead
        self.snakeHead.append(self.lead_x)
        self.snakeHead.append(self.lead_y)
        self.snakeList.append(self.snakeHead)
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList [0]
        self.lead_x += self.lead_x_change
        self.lead_y += self.lead_y_change

    def draw_snake(self, snakeList):
        for coord in self.snakeList:
            pygame.draw.rect(gameDisplay, yellow, [coord[0], coord[1], blockSize, blockSize])
        pygame.display.update()

    def eat_self(self):
        for eachSegment in self.snakeList[:-1]:
            if eachSegment == self.snakeHead:
                return True


    def dir_left(self):
        self.lead_x_change = -blockSize
        self.lead_y_change = 0
    def dir_right(self):
        self.lead_x_change = blockSize
        self.lead_y_change = 0
    def dir_down(self):
        self.lead_y_change = blockSize
        self.lead_x_change = 0
    def dir_up(self):
        self.lead_y_change = -blockSize
        self.lead_x_change = 0

class Apple:
    def __init__(self):
        self.x = round((random.randrange(0, displayWidth-blockSize))/blockSize) * blockSize
        self.y = round((random.randrange(0, displayHeight-blockSize))/blockSize) * blockSize

    def draw_apple(self, color):
        self.color = color
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, blockSize, blockSize])

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Object Snake')
clock = pygame.time.Clock()
blockSize = 20
gameOverMsg = Text("Game over, press C to play again or Q to quit", red, None, 25)

def gameLoop():
    gameExit = False
    gameOver = False
    apple = Apple()
    snake = Snake(displayWidth/2, displayHeight/2, 10, 0, 3)
    snakeList = []
    FPS = 15


    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            gameOverMsg.message_to_screen()
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
                    snake.dir_left()
                elif event.key == pygame.K_RIGHT:
                    snake.dir_right()
                elif event.key == pygame.K_DOWN:
                    snake.dir_down()
                elif event.key == pygame.K_UP:
                    snake.dir_up()

        gameDisplay.fill(black)
        apple.draw_apple(red)
        snake.snake_move(snakeList, [])
        gameOver = snake.eat_self()
        
        if snake.lead_x + blockSize > displayWidth or snake.lead_x < 0 or snake.lead_y + blockSize > displayHeight or snake.lead_y < 0:
            gameOver = True

        snake.draw_snake(snake.snakeList)
        pygame.display.update()

        if snake.lead_x > apple.x - blockSize and snake.lead_y > apple.y - blockSize and snake.lead_x < apple.x + blockSize and snake.lead_y < apple.y + blockSize:
            apple = Apple()
            apple.draw_apple(red)
            snake.snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
