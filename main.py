import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
screen_width = 1280
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Battle")

# load assets
background = pygame.image.load("assets/space-background.png")
ship = pygame.image.load("assets/ship.png")

game_on = True


def draw_background():
    screen.blit(background, (0, 0))


def draw_ship():
    screen.blit(ship, (screen_width / 2, screen_height / 2))


while game_on:

    clock.tick(fps)

    # draw background
    draw_background()

    # draw ship
    draw_ship()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    pygame.display.update()

pygame.quit()
