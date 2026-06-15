import re
import sys

string = str
def isalphacheck(input_variable):
    if input_variable.isalpha(): # Check if input contains ONLY alphabet characters and entirely rejects any numbers or symbols
        return f"The input is a valid text string: {type(input_variable).__name__}"
    else:
        return f"Rejected: The input contains non-alphabetic characters, which is not a valid text-based string."
        exit(0)
print("Welcome to Mad Libs!")
storymode = input("Which madlib would you like to play? 1, 2, or 3: ")
if storymode == "1":
        noun1 = input("Enter a noun: ")
        result = isalphacheck(noun1)
        print(f"Input: {noun1!r} => {result}")
        if not isinstance(noun1, str) or not noun1.strip():
            print("You must enter text")
            exit(0)
        noun2 = input("Enter another noun: ")
        for inp in noun1:
            result = isalphacheck(inp)
        print(f"Input: {inp!r} => {result}")
        adjective1 = input("Enter an adjective: ")
        isalphacheck(adjective1)
        adjective2 = input("Enter another adjective: ")
        isalphacheck(adjective2)
        verb1 = input("Enter a verb: ")
        isalphacheck(verb1)
        verb2 = input("Enter another verb: ")
        isalphacheck(verb2)
        story = "Once upon a time there was a " + adjective1 + " " + noun1 + " who loved to " + verb1 + ". The " + noun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ", So the " + noun1 + " " + verb1 +" over to the " + noun2 + " and they " + verb2 + " all day long."

elif storymode == "2":
    noun1 = input("Enter a noun: ")
    isalphacheck(noun1)
    noun2 = input("Enter another noun: ")
    isalphacheck(noun2)
    adjective1 = input("Enter an adjective: ")
    isalphacheck(adjective1)
    adjective2 = input("Enter another adjective: ")
    isalphacheck(adjective2)
    verb1 = input("Enter a verb: ")
    isalphacheck(verb1)
    verb2 = input("Enter another verb: ")
    isalphacheck(verb2)
    pronoun1 = input("Enter a name for your character:")
    isalphacheck(pronoun1)
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