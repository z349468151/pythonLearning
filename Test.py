import pygame
import sys


class Ship(object):
    def __init__(self):
        self.image = pygame.image.load('AlienGame/images/ship.png')


def check_events(ship_rect, screen_rect, move_left, move_right, move_up, move_down):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and move_left:
                move_left = True
                ship_rect.centerx -= 1
            elif event.key == pygame.K_RIGHT and ship_rect.right < screen_rect.right:
                move_right = True
                ship_rect.centerx += 1
            elif event.key == pygame.K_UP and ship_rect.top > 0:
                move_up = True
                ship_rect.centery -= 1
            elif event.key == pygame.K_DOWN and ship_rect.bottom < screen_rect.bottom:
                move_down = True
                ship_rect.centery += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False


def run_game():
    pygame.init()
    ship = Ship()
    screen = pygame.display.set_mode((800, 600))
    ship_rect = ship.image.get_rect()
    screen_rect = screen.get_rect()
    bg_color = (230, 230, 230)
    ship_rect.center = (screen_rect.centerx, screen_rect.centery)
    move_left = False
    move_right = False
    move_up = False
    move_down = False
    while True:
        check_events(ship_rect, screen_rect, move_left, move_right, move_up, move_down)
        screen.fill(bg_color)
        screen.blit(ship.image, ship_rect)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
