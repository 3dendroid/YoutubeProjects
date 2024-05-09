import random

number = random.randint(0, 10000)

tries = 0
found = False

while not found:
    guess = int(input("Guess a number between 0 and 10000: "))
    tries += 1
    if guess == number:
        found = True
        print(f"You found the number in {tries} tries!")
    elif guess > number:
        print(f"The number you are looking for is less then {guess}!")
    else:
        print(f"The number you are looking for is greater then {guess}!")
