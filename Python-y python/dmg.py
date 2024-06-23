import random

Power = int(input("enter your strength "))
magickpower = int(input("enter your magick power "))
lv = int(input("enter your level "))

dmg = ((Power * random.randint(1, 1125))/100 - magickpower) * (2 + magickpower * (lv + magickpower))

print("The average amount of damage you with hit with is ", dmg)