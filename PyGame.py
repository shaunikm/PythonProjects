import pygame, time

pygame.init()

display_width = 1040
display_height = 780

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Rocket Ride')
clock = pygame.time.Clock()


rocketImg = pygame.image.load("C:\\Users\\shaun\\AppData\\Local\\Programs\\Python\\Python38-32\\Pygame game\\spacecraft-rocket-cartoon-ship-cartoon-rocket-launch-png-clip-boiiii.png")

rocketImg = pygame.transform.scale(rocketImg, (270, 195))

def rocket(x,y):
    gameDisplay.blit(rocketImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (round(display_width/2), round(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You crashed!', 115)

def game_loop():
    x = 400
    x_change = 0
    y = 575
    y_change = 0
    game_exit = False
    rocket_width = rocketImg.get_width()
    rocket_height = rocketImg.get_height()
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white)
        rocket(x,y)

        if x > display_width - rocket_width or x < 0 or y > display_height - rocket_height or y < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()