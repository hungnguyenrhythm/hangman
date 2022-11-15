# Members: Hung Nguyen and Subhan Aamir
# CRN: 84158
# Section: 002
# Project: Hangman

'''
Purpose: Create a basic hangman, where the computer generates a word and we have to guess that letter.
Precondition: A random word was chosen by the computer, and the user has to guess the characters.
Postcondition: If the character is in the word, put it in, else output a picture of a man getting hanged.
'''
# import random module
import random

# Define function for finding the number of time the letter appears in the word to guess
def num_of_letter(choice, word):
    if choice in word:
        return word.count(choice)
    return 0

# Define function to display the current progress of the player
def display_progress(progress, word, guess, count):
    progress = list(progress)
    word = list(word)
    result = ""
    for i in range(count):
        index = word.index(guess)
        progress.pop(index)
        progress.insert(index, guess)
        word.pop(index)
        word.insert(index, " ")
    for items in progress:
        result += items
    return result

#define function to tell body parts
def body(attempt):
    parts_of_body = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
    print("You now have: ", end= " ")
    if attempt == 1:
        print(parts_of_body[0])
    else:
        for i in range(attempt):    
            print(parts_of_body[i], end= " ")
        print()

# define the main() function:
def main():
    word_lst = ["dog", "cat"]
    word = random.choice(word_lst)
    progress = "_" * len(word)
    fail_attempts = 0
    used_list = []
    while fail_attempts < 6:
        print(f"Your progress is {progress}.")
        guess = input("Guess the character of the word: ")
        while guess in used_list:
            guess = input("The character has been used already, please try another one: ")
        if (guess == "") or (guess == " "):
            print("GAME OVER")
            break
        word_count = num_of_letter(guess, word)
        if word_count > 0:
            print(f"There's {word_count} letter {guess} in the word.")
        else:
            print(f"There's no letter {guess} in the word.")
            fail_attempts += 1
            body(fail_attempts)
        progress = display_progress(progress, word, guess, word_count)
        used_list.append(guess)
        if progress == word:
            print("CONGRADULATIONS YOU WIN")
            break
    if fail_attempts == 6:
        print("GAME OVER")
main()

# Create levels.

