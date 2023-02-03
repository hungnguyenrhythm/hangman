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
        return word.count(choice)   # Return the number of times the letter appears in the word
    return 0    # Return 0 if the letter is not in the word

# Define function to display the current progress of the player
def display_progress(progress, word, guess, count):
    progress = list(progress) # Turn the progress into a list
    word = list(word)   # Turn the word into a list
    result = ""
    # Pop a space out and replace it with the letter for the progress displayment
    for i in range(count):
        index = word.index(guess)
        progress.pop(index)
        progress.insert(index, guess)
        word.pop(index)
        word.insert(index, " ")
    for items in progress:
        result += items # Concatenate all of the items in the list variable progress into variable result and return ity
    return result

# Define function to tell body parts
def body(attempt, word):
    # Output what body parts the user got after guessing a letter wrong.
    parts_of_body = ["Head", "LeftArm", "Body", "RightArm", "LeftLeg", "RightLeg"]
    print("You now have: ", end= " ")
    if attempt == 1:
        print(parts_of_body[0])
    else:
        for i in range(attempt):    
            print(parts_of_body[i], end= " ")
        print()
    if attempt >= 3:
        print()
        print(f"Your hint is: {dict_hint(word)}")
        print()

# Define function to draw body parts
def draw_parts(attempt):
    human = ["  0", "/", "|", "\\", " /", "\\"]
    # Illustrating what body parts the user got after guessing a letter wrong.
    print("|--")
    for index in range(attempt):
        if index == 0 or index == 3 or index == 5:
            print(human[index])
        else:
            print(human[index], end = " ")
    print()
    
def dict_hint(word):
    # A dictionary that contains definitions for the words that were randomly generaated by the computer
    hints = {
        "dog": "The most common pet for people",
        "cat": "A small furry animal with claws and wiskers",
        "ink":  "Secreted from squids and used to write",
        "pet": "A stupid animal that serves as playthings for humans.",
        "god": "A part of religious people's believe",
        "war": "A conflict between two groups",
        "zip": "Something done to a zipper",
        "van": "A vehical used to kidnap underage children",
        "hat": "A cap",
        "eat": "something done to your food",
        "person": "I don't know, singular of people??????",
        "iphone": "Overrated touch-screen phone with expensive prices and cheap components.",
        "vitamin": "Types of minerals found in fruts and the sun",
        "focus": "something needed to do things",
        "attention": "Instagram models need a lot of this",
        "strawberry": "A small, sweet, red fruit",
        "minute": "A way of measuring time",
        "sophisticated": "A highly complicated or developed person",
        "quetzacoatlus": "Extinct ancient flying dinosaurs.",
        "anomalocaris": "Ancient rock lobsters.",
        "smaragdine": "emerald green in color.",
        "chiaroscurist": "use for implying an artist that watches too much european films.",
        "pneumonoultramicroscopicsilicovolcanoconiosis": "The longest",
        "antidisestablishmentarianism": "The third longest",
        "pseudopseudohypoparathyroidism": "The second longest",
        }
    # Find the definition of the word and return that word
    hint = hints[word]
    return hint

# Define function to create the different levels of the game
def select_level(level):
    if level == 1:
        levellist = ["dog", "cat", "ink", "pet", "god", "war", "zip", "van", "hat", "eat"]
    if level == 2:
        levellist = ["person", "iphone", "vitamin", "focus", "attention", "strawberry", "minute"]
    if level == 3:
        levellist = ["sophisticated", "quetzacoatlus", "anomalocaris", "smaragdine", "chiaroscurist"]
    if level == 4:
        levellist = ["pneumonoultramicroscopicsilicovolcanoconiosis", "antidisestablishmentarianism", "pseudopseudohypoparathyroidism"]
    return levellist

# define the main() function:
def main(level):
    word_lst = select_level(level)  # Assign a list of words, based on the difficulty to the variable word_lst
    word = random.choice(word_lst)  # Randomly chooses a word from the list
    progress = "_" * len(word) # Create a progress string with the same length as the word
    fail_attempts = 0   # Set the numbers of fail attempts to 0
    used_list = []  # Create a list to put answer that have been used in
    while fail_attempts < 6:
        print() # Bullsh*t spaces from line 118 to line 120
        print("*" * 12)
        print()
        print(f"Your progress is {progress}.")  # Display the progress
        guess = input("Guess the character of the word(or press ENTER to quit): ")  # Ask the user to input a leter
        while guess in used_list:
            guess = input("The character has been used already, please try another one: ") # Ask the user to input again if the answer has already been used
        if (guess == "") or (guess == " "): # If the user press enter to quit
            print("GAME OVER")
            break
        word_count = num_of_letter(guess, word) # Find the number of time the character appears in the word
        if word_count > 0:  # Output the number of times the characters appear in the word
            print(f"There's {word_count} letter {guess} in the word.")
        else:
            print(f"There's no letter {guess} in the word.")
            fail_attempts += 1
            body(fail_attempts, word) # Display and illustrate body parts if the player's guess is wrong
            draw_parts(fail_attempts)
        progress = display_progress(progress, word, guess, word_count) # Update the progress
        used_list.append(guess)
        if progress == word:
            break
    if progress == word:
        print()
        print(f"you got the word {word}")
        print(F"CONGRADULATIONS YOU WIN LEVEL {level} d(ὃ⍜ ὅ)b")
        print()
        option(level + 1, 0)
    if fail_attempts == 6:
        print("GAME OVER (X_X)")
        option(level, 1)

# Define the option() function to decide to go to the next level or ask to restart if you failed
def option(level, fail):
    if fail == 1:
        choice = input("Do you want to restart(y) or do you want to quit(n): ")
        while (choice != "y") and (choice != "n"):
            choice = input("Please try again: ")
        if choice == "y":
            main(level)
        elif choice == "n":
            print("GOODBYE")
    elif fail == 0:
        if level < 5:
            if level == 1:
                print(f"On to level {level}")
                main(level)
            else:
                choice = input("Press 'y' to continue, or press 'n' to quit: ")
                if choice == "y":
                    print(f"On to level {level}")
                    print()
                    print("*" * 12)
                    print()
                    main(level)
                elif choice == "n":
                    print("GOODBYE")
        elif level == 5:
            print("☆彡(/^ ^)/ CONGRATULATIONS YOU CLEARED ALL OF THE LEVEL!!!! ヘ(^ ^ヘ)☆彡")

# Call the function option() to start the game from level 1
option(1, 0)