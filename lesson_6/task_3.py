# Extracting numbers

array = list(range(1, 101))
new_array = []
i = 0

while i != len(array):
    if array[i] % 7 == 0 and array[i] % 5 != 0:
        new_array.append(array[i])
    i += 1

print("The list with integers that are divisible by 7 but not a multiple of 5 is", new_array)
