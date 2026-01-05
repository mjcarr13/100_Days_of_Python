import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
lives = 6
chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

inputted_letters = []

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

display = list(placeholder)
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess not in alphabet:
        print("Silly goose, choose just one letter!")
    elif guess in inputted_letters:
        print("You have already guessed that letter, try again!")
    elif guess in chosen_word:
        for i in range(len(placeholder)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("".join(display))
        print(f"You have {lives} lives left.\n {hangman_art.stages[lives]}")
    elif guess not in inputted_letters and guess not in chosen_word:
        print(f"{guess} is not in the word, you lose a life.")
        lives -= 1
        print("".join(display))
        print(f"You have {lives} lives left.\n {hangman_art.stages[lives]}")
    inputted_letters.append(guess)
if lives == 0:
    print(f"Out of lives. The word was '{chosen_word}'")
else:
    print("You have won!")


