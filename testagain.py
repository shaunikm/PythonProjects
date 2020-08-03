import pygame, time
import random

pygame.init()

display_width = 1040
display_height = 780

global black
global white
black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Rocket Ride')
clock = pygame.time.Clock()

rocketImg = pygame.image.load(
    "C:\\Users\\shaun\\AppData\\Local\\Programs\\Python\\Python38-32\\Pygame game\\spacecraft-rocket-cartoon-ship-cartoon-rocket-launch-png-clip-boiiii.png")

rocketImg = pygame.transform.scale(rocketImg, (270, 195))


def rocket(x, y):
    gameDisplay.blit(rocketImg, (x, y))


def make_aster(asterx, astery, asterh, asterw, asterc):
    pygame.draw.rect(gameDisplay, asterc, (asterx, astery, asterw, asterh))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (round(display_width / 2), round(display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You lost control of the ship', 50)


def game_loop():
    x = 400
    x_change = 0
    y = 575
    y_change = 0

    aster_startx = random.randrange(0, display_width)
    aster_starty = -600
    aster_speed = 7
    aster_width = 100
    aster_height = 100

    game_exit = False
    rocket_width = rocketImg.get_width()
    rocket_height = rocketImg.get_height()
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
        x += x_change
        y += y_change

        make_aster(aster_startx, aster_starty, aster_height, aster_width, black)
        aster_starty += aster_speed

        gameDisplay.fill(white)

        rocket(x, y)

        if x > display_width + rocket_width / 4 or x < 0 - rocket_width or y > display_height or y < 0 - rocket_height:
            crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
