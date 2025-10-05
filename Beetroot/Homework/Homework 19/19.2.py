def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero")

    if step > 0:
        current = start
        while current < end:
            yield current
            current += step
    else:
        current = start
        while current > end:
            yield current
            current += step

# print(list(in_range(1, 5)))  # [1, 2, 3, 4]
# print(list(in_range(5, 1, -1)))  # [5, 4, 3, 2]
# print(list(range(1, 5)))  # [1, 2, 3, 4]
