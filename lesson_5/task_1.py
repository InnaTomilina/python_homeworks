# The Guessing Game

import random

number = int(input("Please, try to guess what number was generated from 1 to 10: "))
random_name = random.randint(1, 10)

if number == random_name:
    print("Congratulations. You have a good intuition!")
else:
    print(f'Sorry, the generated number is {random_name}. Try again.')
