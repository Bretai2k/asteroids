# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    fps = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill(color="black", rect=None, special_flags=0)

        player.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        fps.tick(60)
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
