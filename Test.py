import pygame
import sys


class Ship(object):
    def __init__(self):
        self.image = pygame.image.load('AlienGame/images/ship.png')


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    ship = Ship()
    screen_rect = screen.get_rect()
    bg_color = (230, 230, 230)
    ship_rect = ship.image.get_rect()
    ship_rect.centerx = screen_rect.centerx
    ship_rect.centery = screen_rect.centery

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.blit(ship.image, screen_rect)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
