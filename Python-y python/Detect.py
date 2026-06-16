r = input() # IGNORE --- Detects if the input is a string, and if it is not, it will print the type of the input and exit the program. If it is a string, it will print the input and its type.
r.strip()
for inp in r:
    result = (inp)
    print(f"Input: {inp!r} => {result}")
print(type(r))