#Exclusive common numbers

from random import randrange

array = []
LEN_ARRAY = 10
# random integers from 0 to 100
EXTREME_NUMBER = 100
i = 0

while i != LEN_ARRAY:
    array.append(randrange(EXTREME_NUMBER))
    i += 1

print(array)
print("The largest number in an array is", max(array))
