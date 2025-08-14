# Функція enumerate(iterable, start=0) повертає ітератор, який генерує кортежі (index, element)
# для кожного елемента в iterable, починаючи з start.

def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield (index, item)
        index += 1

# for i, val in with_index(['a', 'b', 'c'], start=1):
#     print(i, val)
#
# e = enumerate(['a', 'b'])
# w = with_index(['a', 'b'])
#
# print(type(e))  # <class 'enumerate'>
# print(type(w))  # <class 'generator'>
