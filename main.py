
import random

while True:
    computer = ["rock", "paper", "scissor"]
    random_number = random.randint(0, 2)
    computer_input = computer[random_number]
 
    player = input("Choose Between rock, paper, and scissor: ").lower()

    while player not in ["rock", "paper", "scissor"]:
        player = input("Invalid input. Choose Between rock, paper, and scissor: ").lower()

    if player == computer_input:
        print("Tie")
    elif player == "rock" and computer_input == "paper":
        print("Computer Wins")
    elif player == "rock" and computer_input == "scissor":
        print("Player Wins")
    elif player == "paper" and computer_input == "rock":
        print("Player Wins")
    elif player == "paper" and computer_input == "scissor":
        print("Computer Wins")
    elif player == "scissor" and computer_input == "rock":
        print("Computer Wins")
    elif player == "scissor" and computer_input == "paper":
        print("Player Wins")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Do you want to play again? (yes/no): ").lower()

    if play_again == "no":
        break