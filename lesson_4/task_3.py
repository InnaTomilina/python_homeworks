# The math quiz program.

from random import randrange

a = randrange(0, 20)
b = randrange(0, 20)
c = a + b

result = int(input(f"What´s the result of {a} + {b} = ? "))
if result == c:
    print("Your answer is correct!")
else:
    print("Check your answer. Something is wrong.")
