import random

# генерація списку
nums = []
i = 0

# Цикл генерує число в заданому діапазоні зі згенерованого списку
while i < 10:
    nums.append(random.randint(1, 120))
    i += 1

# генерується найбільше число
top_nums = nums[0]
i = 1

#
while i < len(nums):
    if nums[i] > top_nums:
        top_nums = nums[i]
    i += 1
print(f'List of generated numbers: {nums}')
print(f'Top number: {top_nums}')
