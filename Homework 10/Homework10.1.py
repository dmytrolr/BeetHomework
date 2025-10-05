# Task 1
#
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError('Це помилка індексу!')

def handehoch_error():
    try:
        oops()
    except IndexError:
        print('Це помилка індексу!')

handehoch_error()


# def oops():
#     raise KeyError('Це помилка ключа!')
#
# def handehoch_error():
#     try:
#         oops()
#     except IndexError:
#         print(Це помилка індексу!')
#
# handehoch_error()

# отримали помилку:

# Traceback (most recent call last):
# File "/home/dmytro/Desktop/Python/Beetroot/Homework/Homework 10/Homework10.1.py", line 20, in oops
#     raise KeyError('Це помилка ключа!')
# KeyError: 'Це помилка ключа!'

# для того щоб перехопити додатково KeyError потрібно змінити не лише oops() а і except():
# except(IndexError, KeyError):
#   print('Перехоплена помилка індексу і помилка ключа')
