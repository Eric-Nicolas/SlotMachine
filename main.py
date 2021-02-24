# coding: utf-8
import pygame
import os
import random

__author__ = 'Eric-Nicolas'

pygame.init()

FRUITS = ('orange', 'cherry', 'pineapple', 'watermelon', 'golden_apple')
TOKENS = (5, 15, 50, 150, 10000)

IMAGES = []
for fruit in FRUITS:
    IMAGES.append(pygame.image.load(os.path.join('assets', fruit + '.png')))

SLOT_IMG = pygame.image.load(os.path.join('assets', 'slot.png'))
RED_CROSS_IMG = pygame.image.load(os.path.join('assets', 'red_cross.png'))

FRUITS_ASSOCIATED = {}
for i in range(len(FRUITS)):
    FRUITS_ASSOCIATED[FRUITS[i]] = (IMAGES[i], TOKENS[i])

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
    for item in seq:
        if item != seq[0]:
            return False
    return True


def draw_crosses() -> None:
    WIN.blit(RED_CROSS_IMG, LEFT)
    WIN.blit(RED_CROSS_IMG, MIDDLE)
    WIN.blit(RED_CROSS_IMG, RIGHT)


def draw_fruits(fruits: list) -> None:
    WIN.blit(FRUITS_ASSOCIATED[fruits[0]][0], LEFT)
    WIN.blit(FRUITS_ASSOCIATED[fruits[1]][0], MIDDLE)
    WIN.blit(FRUITS_ASSOCIATED[fruits[2]][0], RIGHT)


def draw_text(label: pygame.Surface) -> None:
    WIN.blit(label, (WIDTH - label.get_width() - 10, HEIGHT - label.get_height() - 10))


def main() -> None:
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
                random_fruits = random.choices(FRUITS, weights=(40, 25, 20, 10, 5), k=3)
                if has_same_value(random_fruits):
                    tokens += FRUITS_ASSOCIATED[random_fruits[0]][1]

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
