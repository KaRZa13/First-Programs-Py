import random

print("Hello, welcome to a basic dice game based on luck")
print("You have to roll the dice anytime you want but if you overtake 21, you lose")
print("The player closest to 21 wins the game")


def roll_dice():
    return random.randint(1, 6)


def play_game():
    player1_score = 0
    player2_score = 0

    while player1_score < 21 and player2_score < 21:
        choix = input("Player 1, it's your turn! Do you want to roll the dice? (o/n)")
        if choix == "o":
            dice_result = roll_dice()
            print(f"The dice shows: {dice_result}")
            player1_score += dice_result
            print(f"Your score is: {player1_score}")
            print("-----------------------------------")
        else:
            break

        choix = input("Player 2, it's your turn! Do you want to roll the dice? (o/n)")
        if choix == "o":
            dice_result = roll_dice()
            print(f"The dice shows: {dice_result}")
            player2_score += dice_result
            print(f"Your score is: {player2_score}")
            print("-----------------------------------")
        else:
            break

    if player1_score > 21 and player2_score > 21:
        print("Both players lose. Nobody is closest to 21.")
    elif player1_score > 21:
        print("Player 1 loses. Player 2 wins!")
    elif player2_score > 21:
        print("Player 2 loses. Player 1 wins!")
    else:
        if 21 - player1_score < 21 - player2_score:
            print("Player 1 wins!")
        elif 21 - player2_score < 21 - player1_score:
            print("Player 2 wins!")
        else:
            print("It's a draw! Both players have the same score.")

play_game()
