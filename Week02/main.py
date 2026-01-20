# COMP2152 Lab 2
# Rock Paper Scissors Game
# Rojan Jafarnezhad - 101561560
import random

choices = ["Rock", "Paper", "Scissors"]

print("\n----- Welcome to the game! -----")

playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice - 1]
    computerChoiceIndex = choices[computerChoice - 1]

    print("\nYou chose: ", playerChoiceIndex)
    print("Computer chose: ", computerChoiceIndex)

    # determine the winner using if else
    if playerChoice == computerChoice:
        print("\nIt's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("\nRock beats Scissors - You won!")
    elif playerChoice == 2 and computerChoice == 1:
        print("\nPaper beats Rock - You won!")
    elif playerChoice == 3 and computerChoice == 2:
        print("\nScissors beat Paper - You won!")
    else:
        print("You lost!")

    if playerChoiceIndex == 0:
        print("You didn't pick the classic Rock...")