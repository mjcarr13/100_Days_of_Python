#import art module for later use
import art
#import random module for later use
import random
#lives tally initiated
lives = -1
#guessed number variable initiated
guess = -1
#random number initiated between 1 and 100 with each reload
number_to_guess = random.choice(list(range(1,100)))
#import art logo

#function to run incorrect guess - remove a life and check if guess higher/lower. Print text accordingly
def check_guess(guessed_num, num_to_check):
    if guessed_num == num_to_check:
        return
    else:
        global lives
        lives -=1
        if guessed_num > num_to_check:
            print("Too High."
                    "\nGuess Again.")
        else:
            print("Too low."
                    "\nGuess Again.")



print(art.logo)
#print welcome messages
print("Welcome to the Number Guessing Game! "
      "\nI'm thinking of a number between 1 and 100.")
#decide difficulty setting via user input
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
#set number of lives depending on difficulty level
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

#initiate while loop. As long as the player has more than 0 lives and hasn't guessed the number
while lives > 0 and guess != number_to_guess:
    #take guess as an input, converting to a integer
    guess = int(input(f"You have {lives} attempts remaining to guess the number. \n"
          f"Make a guess:"))
#run earlier checking function to remove life and print higher/lower info
    check_guess(guess, number_to_guess)
#if user either guesses number or lives run out
else:
#if guess is correct, print victory statement and the correct number
    if guess == number_to_guess:
        print(f"You got it! The number was {number_to_guess}")
#if lives have run out, print loss statement and artwork.
    elif lives == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        print(art.fail)

