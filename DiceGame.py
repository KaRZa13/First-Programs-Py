import random

print("Hello, welcome to a basic dice game based on luck")
print("You have to pick a number between 1 and 6, if you're correct, you win 1 point")
print("The first player with 3 points win the game")


def roll_dice():
    return random.randint(1, 6)


def play_game():
    player1_score = 0
    player2_score = 0

    while player1_score < 3 and player2_score < 3:
        print("Player 1, it's your turn !")
        player1_choice = int(input("Pick a number between 1 and 6 : "))
        dice_result = roll_dice()
        print("The dice shows : ", dice_result)

        if dice_result == player1_choice:
            player1_score += 1
            print("Well done you win 1 point !")

        else:
            print("Oh no ! No point for Player 1")

        print("The score is ", player1_score, "vs", player2_score)
        print("----------------------------")

        if player1_score < 3:
            print("Player 2, it's your turn !")
            player2_choice = int(input("Pick a number between 1 and 6 : "))
            dice_result = roll_dice()
            print("The dice shows : ", dice_result)

            if dice_result == player2_choice:
                player2_score += 1
                print("Well done you win 1 point !")

            else:
                print("Oh no ! No point for player 2")

            print("The score is ", player1_score, "vs", player2_score)
            print("----------------------------")

    if player1_score == 3:
        print("Player 1 win the game !")
    else:
        print("Player 2 win the game !")


if __name__ == "__main__":

    play_game()
