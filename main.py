import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    in_game = True

    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False

        screen.fill("black")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()