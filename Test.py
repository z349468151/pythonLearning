import pygame
import sys


class Ship(object):
    def __init__(self):
        self.image = pygame.image.load('AlienGame/images/ship.png')


def check_events(move_left, move_right, move_up, move_down):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
    return move_left, move_right, move_up, move_down


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
        move_left, move_right, move_up, move_down = check_events(move_left, move_right, move_up, move_down)
        print(ship_rect.left)
        if move_left and ship_rect.left > 0:
            ship_rect.centerx -= 1
        elif move_right and ship_rect.right < screen_rect.right:
            ship_rect.centerx += 1
        elif move_up and ship_rect.top > 0:
            ship_rect.centery -= 1
        elif move_down and ship_rect.bottom < screen_rect.bottom:
            ship_rect.centery += 1
        screen.fill(bg_color)
        screen.blit(ship.image, ship_rect)
        pygame.display.flip()


def run_game1():
    pygame.init()
    pygame.display.set_mode((800, 600))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    run_game()
