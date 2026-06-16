import string
import random

def generatekey(length):
    characters = string.printable
    key = ''.join(random.choice(characters) for i in range(length))
    return key

print(str(generatekey(16)))