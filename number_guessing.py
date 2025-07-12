"""
Number Guessing Game
--------------------
A fun command-line game where:
- Player guesses a number between 1-100
- Shows number of attempts
- Input validation and play again option
"""

import random
import time

def number_guess():
    """
    Runs an interactive Number Guessing Game:
    - Generates a random number
    - Player keeps guessing until correct
    - Tracks attempts
    - Offers to play again after each game
    """

#Outer while loop for playing again and again
    while True:
        attempts = 0
        comp_choice = random.randint(1,100)

        print("\n" + "-" * 40)
        print("\n🎲 Welcome to Number Guessing Game! I have picked a number between 1 and 100.")
        time.sleep(2)

    
#User Input
        while True:
            print("\n" + "-" * 40)
            try:
                user = int(input("Enter your choice : "))
            except ValueError:
                print("Invalid choice..Enter a number")
                continue

#Winning Condition
            if user < comp_choice:
                print("Too low.. 📉")
                attempts += 1
            elif user > comp_choice:
                print("Too high.. 📈 ")
                attempts += 1
            else:
                print("You got it! 🎉 ")
                time.sleep(1)
                attempts += 1
                print(f"The number was : {comp_choice}")
                print(f"The attempts you took : {attempts}")
                print("-" * 40)
                break

#play again option
        while True:
            play_again = input("Wanna play again yes/no : ").lower()

            if play_again in ["yes" , "no"]:
                break
            print("Invalid choice...Type yes/no")

        if play_again == "no":
            print("Thanks for playing 😀")
        else:
            print("Starting a new game! 🎲")
            time.sleep(1)
            continue
                

if __name__ == "__main__":
    number_guess()