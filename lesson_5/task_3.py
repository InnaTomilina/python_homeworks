# Words combination

import random

word = input("Please, enter any word: ")
n = 0

while n != 5:
    print("".join(random.choice(word) for i in range(len(word))))
    n += 1
