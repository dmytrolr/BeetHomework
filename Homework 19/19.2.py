def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero")

    if step > 0:
        current = start
        while current <= end:
            yield current
            current += step

    else:
        current = start
        while current >= end:
            yield current
            current += step

# print(list(in_range(0, 5)))
#
# print(list(in_range(2, 10, 2)))
#
# print(list(in_range(10, 2, -2)))
