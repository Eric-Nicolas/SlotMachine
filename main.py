# coding: utf-8
import random

__author__ = 'Eric-Nicolas'

ORANGE = 'orange'
CHERRY = 'cherry'
PINEAPPLE = 'pineapple'
WATERMELON = 'watermelon'
GOLDEN_APPLE = 'golden apple'


def has_same_value(seq: list) -> bool:
    for i in seq:
        if i != seq[0]:
            return False
    return True


def main() -> None:
    print("Welcome to the machine slot GravenFruitiiii!")

    fruits = [ORANGE, CHERRY, PINEAPPLE, WATERMELON, GOLDEN_APPLE]
    tokens_associated = {
        ORANGE: 5,
        CHERRY: 15,
        PINEAPPLE: 50,
        WATERMELON: 150,
        GOLDEN_APPLE: 10000
    }

    tokens = 0

    # returns k elements of fruits; each item has a probability written in the weights parameter
    random_fruits = random.choices(fruits, weights=(40, 25, 20, 10, 5), k=3)
    print(random_fruits)

    if has_same_value(random_fruits):
        print("3x " + random_fruits[0] + " - You win " + str(tokens_associated[random_fruits[0]]) + " tokens!")
        tokens += tokens_associated[random_fruits[0]]


if __name__ == '__main__':
    main()
