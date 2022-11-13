def foo(a, b):
    try:
        result = int(a) ** 2 / int(b)
        return result
    except ValueError:
        print("Sorry, you putted invalid data")
    except ZeroDivisionError:
        print("Division by zero")


a1 = input("Enter a number: ")
b1 = input("Enter a number: ")
print(foo(a1, b1))
