from lesson_9.task_1_1 import find_sum


def count_numbers(list):
    return len(list)


my_lst = [10, 20, 30]


def main():
    print("The average number is: ", find_sum(my_lst) / count_numbers(my_lst))


if __name__ == "__main__":
    main()
