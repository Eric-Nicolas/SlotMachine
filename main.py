# coding: utf-8
import pygame
import os
import random

__author__ = 'Eric-Nicolas'

pygame.init()

ORANGE = 'orange'
CHERRY = 'cherry'
PINEAPPLE = 'pineapple'
WATERMELON = 'watermelon'
GOLDEN_APPLE = 'golden_apple'

ORANGE_IMG = pygame.image.load(os.path.join('assets', ORANGE + '.png'))
CHERRY_IMG = pygame.image.load(os.path.join('assets', CHERRY + '.png'))
PINEAPPLE_IMG = pygame.image.load(os.path.join('assets', PINEAPPLE + '.png'))
WATERMELON_IMG = pygame.image.load(os.path.join('assets', WATERMELON + '.png'))
GOLDEN_APPLE_IMG = pygame.image.load(os.path.join('assets', GOLDEN_APPLE + '.png'))

SLOT_IMG = pygame.image.load(os.path.join('assets', 'slot.png'))

IMAGES_ASSOCIATED = {
    ORANGE: ORANGE_IMG,
    CHERRY: CHERRY_IMG,
    PINEAPPLE: PINEAPPLE_IMG,
    WATERMELON: WATERMELON_IMG,
    GOLDEN_APPLE: GOLDEN_APPLE_IMG
}

TOKENS_ASSOCIATED = {
    ORANGE: 5,
    CHERRY: 15,
    PINEAPPLE: 50,
    WATERMELON: 150,
    GOLDEN_APPLE: 10000
}

WIDTH, HEIGHT = 800, 400
WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot Machine")

WHITE = (255, 255, 255)

CLOCK = pygame.time.Clock()
FPS = 60

Y = HEIGHT // 2 + 56

LEFT = (226, Y)
MIDDLE = (327, Y)
RIGHT = (428, Y)


def has_same_value(seq: list) -> bool:
    for i in seq:
        if i != seq[0]:
            return False
    return True


def main() -> None:
    fruits = [ORANGE, CHERRY, PINEAPPLE, WATERMELON, GOLDEN_APPLE]
    random_fruits = []
    tokens = 0

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # returns k elements of fruits; each item has a probability written in the weights parameter
                random_fruits = random.choices(fruits, weights=(40, 25, 20, 10, 5), k=3)
                print(random_fruits)

                if has_same_value(random_fruits):
                    print("3x " + random_fruits[0] + " - You win " + str(TOKENS_ASSOCIATED[random_fruits[0]]) + " tokens!")
                    tokens += TOKENS_ASSOCIATED[random_fruits[0]]

        WIN.fill(WHITE)
        WIN.blit(SLOT_IMG, (0, 0))

        if random_fruits:
            WIN.blit(IMAGES_ASSOCIATED[random_fruits[0]], LEFT)
            WIN.blit(IMAGES_ASSOCIATED[random_fruits[1]], MIDDLE)
            WIN.blit(IMAGES_ASSOCIATED[random_fruits[2]], RIGHT)

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
