# Members: Hung Nguyen and Subhan Aamir
# CRN: 84158
# Section: 002
# Project: Hangman

'''
Purpose: Create a basic hangman, where the computer generates a word and we have to guess that letter.
Precondition: A random word was chosen by the computer, and the user has to guess the characters.
Postcondition: If the character is in the word, put it in, else output a picture of a man getting hanged.

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
# Use Turtle for the body display
'''

# import random module
import random

# import turtle module
import turtle

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

# Define function to tell body parts
def body(attempt):
    parts_of_body = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
    drawP_O_B = [draw_head, draw_body, draw_Larm, draw_Rarm, draw_Lleg, draw_Rleg]
    print("You now have: ", end= " ")
    if attempt == 1:
        print(parts_of_body[0])
        drawP_O_B[0]()
    else:
        for i in range(attempt):    
            print(parts_of_body[i], end= " ")

        drawP_O_B[(attempt - 1)]()
        print()

# Define function to draw body parts
def draw_parts(attempt):
    drawP_O_B = [draw_head, draw_body, draw_Larm, draw_Rarm, draw_Lleg, draw_Rleg]
    drawP_O_B[attempt - 1]()
    print()

# Define function to create the different levels of the game
def select_level(level):
    if level == 1:
        levellist = ["dog", "cat"]
    if level == 2:
        levellist = ["person", "iphone"]
    if level == 3:
        levellist = ["supercalafragilisticexpialadoshist"]
    return levellist

# Define the helper function to decide to go to the next level or ask to restart if you failed
def option(level, fail):
    if fail == 1:
        choice = input("Do you want to restart(y) or do you want to quit(n): ")
        if (choice != "y") or (choice != "n"):
            choice = input("Please try again: ")
        if choice == "y":
            main(level)
        elif choice == "n":
            print("GOODBYE")
    elif fail == 0:
        if level < 4:
            if level == 1:
                print(f"On to level {level}")
                main(level)
            else:
                choice = input("Do you want to go to the next level(y) or do you want to quit(n): ")
                if choice == "y":
                    print(f"On to level {level}")
                    main(level)
                elif choice == "n":
                    print("GOODBYE")
        elif level == 4:
            print("You Finished All The Levels CONGRADULATIONS!!!!!")
            

# Define function to draw the head
def draw_head():
    turtle.speed(0)

    turtle.penup()
    turtle.setposition(10, 200)  
    turtle.pendown()
    turtle.fillcolor("#DBB267")
    turtle.begin_fill()

    turtle.circle(50)
    
    turtle.end_fill()

# Define function to draw the body
def draw_body():

    draw_head()

    turtle.penup()
    turtle.setposition(-55, 200)  
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(125)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)


    turtle.end_fill()

# Define function to draw the left arm
def draw_Larm():

    draw_body()

    turtle.penup()
    turtle.setposition(-55, 170)  
    turtle.pendown()
    turtle.fillcolor("#DBB267")
    turtle.begin_fill()

    turtle.left(180)

    for i in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)


    turtle.end_fill()

# Define function to draw the right arm
def draw_Rarm():

    draw_Larm()

    turtle.penup()
    turtle.setposition(70, 170)  
    turtle.pendown()
    turtle.fillcolor("#DBB267")
    turtle.begin_fill()

    turtle.left(180)

    for i in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)


    turtle.end_fill()

# Define function to draw the left leg
def draw_Lleg():

    draw_Rarm()

    turtle.penup()
    turtle.setposition(-5, 0)  
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()

    turtle.left(180)

    for i in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)


    turtle.end_fill()

# Define function to draw the right leg
def draw_Rleg():

    draw_Lleg()

    turtle.penup()
    turtle.setposition(20, 0)  
    turtle.pendown()
    turtle.fillcolor("grey")
    turtle.begin_fill()

    turtle.left(180)

    for i in range(2):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)


    turtle.end_fill()

# define the main() function:
def main(level):
    word_lst = select_level(level)
    word = random.choice(word_lst)
    progress = "_" * len(word)
    fail_attempts = 0
    used_list = []
    while fail_attempts < 6:
        print(f"Your progress is {progress}.")
        guess = input("Guess the character of the word(or press ENTER to quit): ")
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
            draw_parts(fail_attempts)
        progress = display_progress(progress, word, guess, word_count)
        used_list.append(guess)
        if progress == word:
            print(f"you got the word {word}")
            print(F"CONGRADULATIONS YOU WIN LEVEL {level}")
            level += 1
            option(level, 0)
    if fail_attempts == 6:
        print("GAME OVER")
        option(level, 1)

option(1, 0)