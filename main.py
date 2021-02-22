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
RED_CROSS_IMG = pygame.image.load(os.path.join('assets', 'red_cross.png'))

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
BLACK = (0, 0, 0)

FONT = pygame.font.Font(None, 36)

Y = HEIGHT // 2 + 56
LEFT = (226, Y)
MIDDLE = (327, Y)
RIGHT = (428, Y)

CLOCK = pygame.time.Clock()
FPS = 60


def has_same_value(seq: list) -> bool:
    for i in seq:
        if i != seq[0]:
            return False
    return True


def draw_crosses() -> None:
    WIN.blit(RED_CROSS_IMG, LEFT)
    WIN.blit(RED_CROSS_IMG, MIDDLE)
    WIN.blit(RED_CROSS_IMG, RIGHT)


def draw_fruits(fruits: list) -> None:
    WIN.blit(IMAGES_ASSOCIATED[fruits[0]], LEFT)
    WIN.blit(IMAGES_ASSOCIATED[fruits[1]], MIDDLE)
    WIN.blit(IMAGES_ASSOCIATED[fruits[2]], RIGHT)


def draw_text(label: pygame.Surface) -> None:
    WIN.blit(label, (WIDTH - label.get_width() - 10, HEIGHT - label.get_height() - 10))


def main() -> None:
    fruits = [ORANGE, CHERRY, PINEAPPLE, WATERMELON, GOLDEN_APPLE]
    random_fruits = []
    tokens = 0

    is_running = True
    while is_running:
        tokens_label = FONT.render("Tokens: " + str(tokens), True, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # returns k elements of fruits; each item has a probability written in the weights parameter
                random_fruits = random.choices(fruits, weights=(40, 25, 20, 10, 5), k=3)
                if has_same_value(random_fruits):
                    tokens += TOKENS_ASSOCIATED[random_fruits[0]]

        WIN.fill(WHITE)
        WIN.blit(SLOT_IMG, (0, 0))

        if not random_fruits:  # if the list is empty
            draw_crosses()
        else:
            draw_fruits(random_fruits)

        draw_text(tokens_label)

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
