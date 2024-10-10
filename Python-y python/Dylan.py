from ctypes.wintypes import PINT
from pickletools import string1
import re
import sys

#def is_string(a):
#  return isinstance(a, str) is not None # Check Character class

#string1 = print("Is this a string?")
#choice = input()

#print(type(choice)) # Print whether or not the character class is a text-based string
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

# Example usage:
inputs = input()
#[
#    "Hello, world!",     # Valid text
#    "",                  # Empty string
#    "   ",              # Whitespace string
#    123,                # Integer
#    45.67,              # Float
#    [1, 2, 3],          # List
#    {'key': 'value'},   # Dictionary
#    None                 # NoneType
#]

for inp in inputs:
    result = detect_text_type(inp)
    print(f"Input: {inp!r} => {result}")