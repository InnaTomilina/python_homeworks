# Exclusive common numbers

from random import randrange

#generate two lists with the length of 10
array_1 = []
array_2 = []
LEN_ARRAY = 10
i = 0

while i != LEN_ARRAY:
    array_1.append(randrange(1, 10))
    array_2.append(randrange(1, 10))
    i += 1

#create 3d list containing the common integers between the 2 initial lists without any duplicates
array_3 = []
k = 0

while k != LEN_ARRAY:
    if array_1[k] in array_2 and array_1[k] not in array_3:
        array_3.append(array_1[k])
    k += 1

print(array_1)
print(array_2)
print(array_3)
