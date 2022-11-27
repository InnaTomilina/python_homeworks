def my_pow(item, power):
    return item**power

powers = [1, 2, 5, 8, 10]
a = [2, 4, 3, 1]

print(list(map(my_pow, a, powers)))


