def foo(func):
    return func.__code__.co_nlocals


def test():
    a = 1
    b = 2
    c = a * b
    return c


print(foo(test))
