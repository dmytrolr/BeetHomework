class Mathematician:
    def square_nums(self, numbers):
        return [num ** 2 for num in numbers]

    def remove_positive_nums(self, numbers):
        return [num for num in numbers if num <= 0]

    def year_filter(self, years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positive_nums([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.year_filter([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
        