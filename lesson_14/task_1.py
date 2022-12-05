def logger(func):
    def inner(*args):
        print(f"{ func.__name__ } called with {', '.join(map(str, args))}")
        func(*args)

    return inner


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg**2 for arg in args]


add(2, 3)
square_all(1, 2, 3, 4)
