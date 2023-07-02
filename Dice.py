import random


def roll_dice():
    return random.randint(1, 6)


dice1 = roll_dice()
dice2 = roll_dice()

print("Le premier dé montre : ", dice1)
print("Le second dé montre : ", dice2)

total = dice1 + dice2

print("Le total est : ", total)
