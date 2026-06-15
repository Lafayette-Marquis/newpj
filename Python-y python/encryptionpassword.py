import string
import random
import re

def generatekey(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(characters) for i in range(length))
    return key

str(generatekey(16))