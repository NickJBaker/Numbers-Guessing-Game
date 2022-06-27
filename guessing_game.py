"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    high_score = []
    play_again = ""
    while True:
        if play_again.lower() == "y":
            print("\nYour high score: {}".format(min(high_score)))
            if min(high_score) == 1:
                print("You've got the highest score possible!! You rock!")
        print(("-" * 36) + "\nWelcome to the Number Guessing Game!\n" + ("-" * 36))
        random_number = random.randrange(1, 11)
        try:
            players_guess = int(input("\nPlease guess a number between 1 and 10: "))
            
            counter = 1
            while players_guess != random_number:
                if players_guess > 10 or players_guess < 1:
                    print("The number you guess must be within the range of 1-10! Please try again.\n")
                    counter -= 1
                elif players_guess > random_number:
                    print("It's lower!\n")
                else:
                    print("It's higher!\n")
                players_guess = int(input("Please guess another number between 1 and 10: "))
                counter += 1
            print("Congradulations!! You got it correct! It took you {} tries!".format(counter))
            
            play_again = input("Would you like to play again? (Y/N) ")
            while play_again.lower() != "y" and play_again.lower() != "n":
                print("You must enter either Y or N to proceed!")
                play_again = input("Would you like to play again? (Y/N) ")
            if play_again.lower() == "y":
                high_score.append(counter)
                continue
            elif play_again.lower() == "n":
                print("Thanks for playing!!")
                break
        except ValueError:
            print("You must enter a number in order to play the game. Please try again!\n")

# Kick off the program by calling the start_game function.
start_game()