class Mathematician:
    def square_nums(self, numbers):
        return list(map(lambda num: num * num, numbers))

    def remove_positives(self, numbers):
        return list(filter(lambda num: num < 0, numbers))

    def filter_leaps(self, years):
        return list(filter(lambda year: year % 4 == 0, years))


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
