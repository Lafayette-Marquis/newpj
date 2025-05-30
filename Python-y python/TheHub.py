from datetime import date
from datetime import time
import random
import string
import re

print("Welcome to the hub! You have a few options, for a password generator, type 'password', for playing mad libs, type 'Mad Libs' for playing rock, paper, scissors, lizard, spock, type 'RPSLS', for calculating a rectangle's area, type 'rectangle'. Which one do you want to use?")

choice = input()


if choice == "password":
    print("Welcome to the random password generator!")

    length = int(input("How long would you like the password to be? in characters: "))

    include_lowercase = input("Include lowercase letters? (y/n) ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'  
    include_numbers = input("Include numbers? (y/n) ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n) ").lower() == 'y'

    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase  

    if include_numbers:
        characters += string.digits

    if include_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for i in range(length))

    print(" ")
    print("Here is your new and generated password:", password)
    print(" ")

elif choice == "Mad Libs" or choice == "mad libs" or choice == "madlibs":
    def detect_text_type(input_variable):
        # Check if the input is a string
        if isinstance(input_variable, str):
            # Further logic can be done to filter out non-text strings if needed (e.g., empty strings)
            if input_variable.strip():  # Reject empty or whitespace-only strings
                return f"The input is a valid text string: {type(input_variable).__name__}"
            else:
                return "Rejected: The input is an empty string."
        else:
            return f"Rejected: The input is of type {type(input_variable).__name__}, which is not a text-based string."
    print("Welcome to Mad Libs!")
    storymode = input("Which madlib would you like to play? 1, 2, or 3: ")
    if storymode == "1":
        noun1 = input("Enter a noun: ")
        for inp in noun1:
            result = detect_text_type(inp)
            print(f"Input: {inp!r} => {result}")
            if result is not type(str):
                print("You must enter text")
                exit(0)
            elif result == type(str): "Good job, that's a string"
        noun2 = input("Enter another noun: ")
        for inp in noun1:
            result = detect_text_type(inp)
        print(f"Input: {inp!r} => {result}")
        adjective1 = input("Enter an adjective: ")
        if adjective1 != type(string):
            print("words must be text, please rerun and try again")
        adjective2 = input("Enter another adjective: ")
        if adjective2 is not type(string):
            print("words must be text, please rerun and try again")
        verb1 = input("Enter a verb: ")
        if verb1 == type(string):
            print("words must be text, please rerun and try again")
        verb2 = input("Enter another verb: ")
        if verb2 == type(string):
            print("words must be text, So thank you!")
        story = "Once upon a time there was a " + adjective1 + " " + noun1 + " who loved to " + verb1 + ". The " + noun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ", So the " + noun1 + " " + verb1 +" over to the " + noun2 + " and they " + verb2 + " all day long."

    elif storymode == "2":
        noun1 = input("Enter a noun: ")
        if noun1 != type(str):
            print("words must be text, please rerun and try again")
        noun2 = input("Enter another noun: ")
        if noun2 != type(str):
            print("words must be text, please rerun and try again")
        adjective1 = input("Enter an adjective: ")
        if adjective1 != type(str):
            print("words must be text, please rerun and try again")
        adjective2 = input("Enter another adjective: ")
        if adjective2 != type(str):
            print("words must be text, please rerun and try again")
        verb1 = input("Enter a verb: ")
        if verb1 != type(string):
            print("words must be text, please rerun and try again")
        verb2 = input("Enter another verb: ")
        if verb2 != type(string):
            print("words must be text, please rerun and try again")
        pronoun1 = input("Enter a name for your character:")
        if pronoun1 != type(str):
            print("words must be text, please rerun and try again")
        story = "Once upon a time, there was a " + adjective1 + " " + noun1 + " who's name was " + pronoun1 + ", " + pronoun1 + " loved to " + verb1 + ". " + pronoun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ". So the " + noun1 + " " + verb1 + " over to the " + noun2 + " and they " + verb2 + " until their parents called them and yelled at them for being home too late."

    else:
        date1 = input("Enter a date: ")
        if date1 != type(str):
            print("Please enter a valid date")
        name1 = input("Enter a name: ")
        if name1 != type(str):
            print("words must be text, please rerun and try again")
        adjective1 = input("Enter an adjective: ")
        if adjective1 != type(str):
            print("words must be text, please rerun and try again")
        noun2 = input("Enter a noun: ")
        if noun2 != type(str):
            print("words must be text, please rerun and try again")
        story = "EXCUSED " + date1 + ": please excuse " + name1 + ", who is far too " + adjective1 + " to be allowed to go to " + noun2 + " class."


    print(" ")
    print(story)
    print(" ")
    print("Thanks for playing Mad Libs!")
    print(" ")

elif choice == "Rock, Paper, Scissors, Lizard, Spock" or choice == "rock, paper, scissors, lizard, spock" or choice == "RPSLS":
    user_threw = input("What do you want to throw - rock, paper, scissors, lizard, or spock? ")
    if (
        (user_threw == "rock") 
        or (user_threw == "paper")
        or (user_threw == "scissors")
        or (user_threw == "spock")
        or (user_threw == "lizard")
    ):
        print(user_threw +' works')
    else:
        print(user_threw + "???? That doesn't work!?")
        exit(0)
    computer_threw = random.choice(["scissors","rock","paper", "lizard", "spock"])
    print("Computer chose " + computer_threw)
    if (computer_threw == user_threw):
        print("It's a tie!")
    elif (
        (computer_threw == "rock" and user_threw == "paper")
        or (computer_threw == "sciossors" and user_threw == "rock")
        or (computer_threw == "paper" and user_threw == "scissors")
        or (computer_threw == "spock" and user_threw == "lizard")
        or (computer_threw == "scissors" and user_threw == "spock")
        or (computer_threw == "rock" and user_threw == "spock")
        or (computer_threw == "lizard" and user_threw == "scissors")
        or (computer_threw == "lizard" and user_threw == "rock")
        or (computer_threw == "spock" and user_threw == "paper")
        or (computer_threw == "paper"  and user_threw == "lizard")
        ):
        print("Good job!  You beat the computer!")    
    else:
        print("The computer won!")

elif choice == "rectangle":
    width = float(input("Enter the width of the rectangle: "))
    if width < 0 or width != type(float or int):
        print("Width cannot be negative nor non-numeric")
    height = float(input("Enter the height of the rectangle: "))
    if height < 0 or height != type(float or int):
        print("Height cannot be negative nor non-numeric")
    area = width * height
    print("The area of the rectangle is", area)
else:
    print("That is not a valid option!")
    exit(0)

print("Thanks for visiting the hub!")