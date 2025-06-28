#Task 1
# from typing import Optional
# def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
#     """
#     Returns  x ^ exp
#     >>> to_power(2, 3) == 8
#     True
#     >>> to_power(3.5, 2) == 12.25
#     True
#     >>> to_power(2, -1)
#     ValueError: This function works only with exp > 0.
#     """
#     pass

from typing import Union, Optional

# Синтаксис ф-ції з умови задачі у мене не працював, виявилось, що Optional приймає
# тільки один тип: або int, або float, або None. А для кількох типів треба використовувати ще Union.
# З'ясував, що існує більш відповідний синтаксис

def to_power(x: int | float | None, exp: int) -> int | float | None:
    if x is None:
        return None
    if exp < 1: # перевірка на хибний exponent
        raise ValueError("This function works only with exp > 0.")
    if exp == 1: # термінальний випадок рекурсії
        return x
    return x * to_power(x, exp - 1)

# print(to_power(2, 3))
# print(to_power(3.5, 2))
# оскільки exponent < 0, тут маємо отримати ValueError
# print(to_power(2, -1))


# Task 2
#
# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#    Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True
#     >>> is_palindrome('sassas')
#     True
#     >>> is_palindrome('o')
#     True
#     pass

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    looking_str = "".join(looking_str.split()) # для виявлення паліндромів з багатьма словами
    if index >= len(looking_str) // 2:
    # Я вирішив, що по суті мене цікавить лише симетрія символів відносно середини аргументу.
    # І коли мій "несправжній ітератор" index дійде до середини, рекурсія припиниться.
        return True
    # А далі треба порівняти:
    if looking_str[index] != looking_str[-(index + 1)]: # порівняння символів зліва looking_str[index]
        # і справа looking_str[-(index + 1)], і якщо вони не сходяться, то:
        return False
    return is_palindrome(looking_str, index + 1)
# print(is_palindrome('mom'))
# print(is_palindrome('sassas'))
# print(is_palindrome('o'))
# print(is_palindrome('а роза упала на лапу азора'))


# Task 3
# from typing import Optional
# def mult(a: int, n: int) -> int:
#     This function works only with positive integers
#     >>> mult(2, 4) == 8
#     True
#     >>> mult(2, 0) == 0
#     True
#     >>> mult(2, -4)
#     ValueError("This function works only with postive integers")


def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    if n == 0:
        return 0
    return a + mult(a, n - 1) # імітація множення через додавання
# print(mult(2, 4))
# print(mult(2, 0))
# print(mult(2, -4))


# ask 4
# def reverse(input_str: str) -> str:
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True

# Ідея в переносі першого символу [0] в кінець аргументу:
def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str
    return reverse(input_str[1:]) + input_str[0]
# print(reverse("hello"))
# print(reverse("o"))
# print(reverse("abracadabra"))

# Task 5
#
# def sum_of_digits(digit_string: str) -> int:
#     >>> sum_of_digits('26') == 8
#     True
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")

def sum_of_digits(digit_string: str) -> int:
    if digit_string == "":
        return 0
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])

# print(sum_of_digits('26'))
# print(sum_of_digits('test'))


