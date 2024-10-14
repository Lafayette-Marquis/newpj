import re
import sys

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
    if adjective1 != type(str):
        print("words must be text, please rerun and try again")
    adjective2 = input("Enter another adjective: ")
    if adjective2 is not type(str):
        print("words must be text, please rerun and try again")
    verb1 = input("Enter a verb: ")
    if verb1 == type(str):
        print("words must be text, please rerun and try again")
    verb2 = input("Enter another verb: ")
    if verb2 == type(str):
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
    if verb1 != type(str):
        print("words must be text, please rerun and try again")
    verb2 = input("Enter another verb: ")
    if verb2 != type(str):
        print("words must be text, please rerun and try again")
    pronoun1 = input("Enter a name for your character:")
    if pronoun1 != type(str):
        print("words must be text, please rerun and try again")
    story = "Once upon a time, there was a " + adjective1 + " " + noun1 + " who's name was " + pronoun1 + ", " + pronoun1 + " loved to " + verb1 + ". " + pronoun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ". So the " + noun1 + " " + verb1 + " over to the " + noun2 + " and they " + verb2 + " until their parents called them and yelled at them for being home too late."

else:
    date1 = input("Enter a date: ")
    if date1 != type(float):
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