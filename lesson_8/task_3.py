# A simple calculator
def subtraction(*args):
    total_1 = args[0]
    for n in args:
        total_1 -= n
    return total_1 + args[0]


def multiplication(*args):
    total_2 = 1
    for n in args:
        total_2 *= n
    return total_2


def make_operation(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return subtraction(*args)
    else:
        return multiplication(*args)


print(make_operation("+", 7, 7, 2))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 7, 6))
