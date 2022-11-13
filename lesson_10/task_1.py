def oops():
    raise IndexError

def main():
    try:
        oops()
    except IndexError:
        print("hello world")

if __name__ == "__main__":
    main()