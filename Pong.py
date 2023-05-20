import pygame

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

class Paddle():
    def __init__(self, width, height, x, y, rect):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = rect

    def collision(self, collideRect):
        return self.rect.colliderect(collideRect)

#variables for first paddle
playerOneWidth, playerOneHeight = 20, 80
playerOnePosX = 0
playerOnePosY = screen.get_height() / 2 - (playerOneHeight / 2)
playerOneRect = pygame.Rect(playerOnePosX, playerOnePosY, playerOneWidth, playerOneHeight)
#create first paddle
paddleOne = Paddle(playerOneWidth, playerOneHeight, playerOnePosX, playerOnePosY, playerOneRect)
#variables for second paddle
playerTwoWidth = 20 
playerTwoHeight = 80
playerTwoPosX = screen.get_width() - playerTwoWidth
playerTwoPosY = screen.get_height() / 2 - (playerTwoHeight / 2)
playerTwoRect = pygame.Rect(playerTwoPosX, playerTwoPosY, playerTwoWidth, playerTwoHeight)
#create second paddle
paddleTwo = Paddle(playerTwoWidth, playerTwoHeight, playerTwoPosX, playerTwoPosY, playerTwoRect)

class Ball():
    def __init__(self, width, height, x, y, rect, speedX, speedY):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = rect
        self.speedX = speedX
        self.speedY = speedY

#variables for ball
ballWidth, ballHeight = 25, 25
ballX = screen.get_width() / 2
ballY = screen.get_height() / 2 - (ballHeight / 2)
ballRect = pygame.Rect(ballX, ballY, ballWidth, ballHeight)
ballSpeedX = 5
ballSpeedY = 5
#create ball
ball = Ball(ballWidth, ballHeight, ballX, ballY, ballRect, ballSpeedX, ballSpeedY)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    #draw player one
    pygame.draw.rect(screen, "red", paddleOne.rect)
    #draw player two
    pygame.draw.rect(screen, "red", paddleTwo.rect)
    #draw game ball
    pygame.draw.rect(screen, "red", ball.rect)

    keys = pygame.key.get_pressed()
    #player one controls
    if keys[pygame.K_w]:
        paddleOne.rect.y -= 7
    if keys[pygame.K_s]:
         paddleOne.rect.y += 7
    #player two controls
    if keys[pygame.K_UP]:
         paddleTwo.rect.y -= 7
    if keys[pygame.K_DOWN]:
        paddleTwo.rect.y += 7

    #player one boundaries
    if  paddleOne.rect.y <= 0:
         paddleOne.rect.y = 0
    if  paddleOne.rect.y >= screen.get_width() - paddleOne.height:
         paddleOne.rect.y = screen.get_width() - paddleOne.height

    #player two boundaries
    if paddleTwo.rect.y <= 0:
        paddleTwo.rect.y = 0
    if paddleTwo.rect.y >= screen.get_width() - paddleTwo.height:
        paddleTwo.rect.y = screen.get_width() - paddleTwo.height

    #ball boundaries
    if ball.rect.y <= 0 or ballRect.y >= screen.get_height() - ball.height:
        ball.speedY = -ball.speedY

    ballRect.x -= ball.speedX
    ballRect.y -= ball.speedY


    if paddleOne.collision(ballRect) or paddleTwo.collision(ballRect):
        ball.speedX = -ball.speedX    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()