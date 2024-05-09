import os
import random
import time

colors = "RGBY"
simon = ""
score = 0

for score in range(0, 10):
    simon += random.choice(colors)
    for color in simon:
        print(color)
        time.sleep(0.5)
        os.system("cls")
    guess = input("Repeat: ")
    os.system("clr")
    if guess != simon:
        break

print(f"Game over. Your score is {score}")
