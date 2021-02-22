# coding: utf-8
import random

__author__ = 'Eric-Nicolas'

ORANGE = 'orange'
CHERRY = 'cherry'
PINEAPPLE = 'pineapple'
WATERMELON = 'watermelon'
GOLDEN_APPLE = 'golden apple'


def main() -> None:
    print("Welcome to the machine slot GravenFruitiiii!")

    fruits = [ORANGE, CHERRY, PINEAPPLE, WATERMELON, GOLDEN_APPLE]
    print(random.choice(fruits))

    random_fruits = []
    while len(random_fruits) < 3:
        fruit = random.choice(fruits)
        if fruit not in random_fruits:
            random_fruits.append(fruit)
    print(random_fruits)


if __name__ == '__main__':
    main()
