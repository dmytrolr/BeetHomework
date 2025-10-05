def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield (index, item)
        index += 1

# data = ['a', 'b', 'c']
# start = 1
#
# print("with_index:")
# for i in with_index(data, start):
#     print(i)
#
# print("\nenumerate:")
# for i in enumerate(data, start):
#     print(i)
