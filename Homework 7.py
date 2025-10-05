# Задача 1
#
# Напишіть програму, яка отримує на вхід деяке речення (рядок) і повертає dict,
# що містить всі унікальні слова як ключі, а кількість входжень - як значення.

story = input("Enter a story: ")

words = story.split()
unique_words = set(words)
word_count = {}
i = 0

while i < len(words):
    word = words [i].strip('"«»,:;-_./?!').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    i += 1
    print()

print('Unique words occurences is: ', word_count)
print()


# Задача 2
#
# Вхідні дані:
#
# stock = {
#  "banana": 6,
#  "apple": 0,
#  "orange": 32,
#  "pear": 15
# }
# prices = {
#  "banana": 4,
#  "apple": 2,
#  "orange": 1.5,
#  "pear": 3
# }
#
# Обчислити загальну ціну на складі, де загальна ціна - це сума
# ціни товару, помножена на кількість цього товару.
# Код повинен повернути словник із сумами цін за типами товарів.

stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}
prices = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

total_price = {} # here I collect total prices
goods = list(stock.keys()) # I need a list with only products names (keys) from stock
total_price[goods[0]] = stock[goods[0]] * prices[goods[0]] # calculating total price
i = 0

while i < len(goods): # iterating goods
    good = goods[i]
    total_price[good] = stock[good] * prices[good] # calculating each key(name) on stock
    i += 1

print('Total price in stock: ', total_price)
print()


# 3
#
# Вправа на розуміння списків
# Використовуючи розуміння списків, складіть список, що містить
# кортежі (i, j), де 'i' від 1 до 10, а 'j' відповідає 'i' у квадраті.

list_1 = []
i = 1

list_1 = [(i, i**2) for i in range(1, 11)] # using a list comprehension
print('Tuples list is ready:', list_1)
print()

#4
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
days_dict = dict(zip(range(1, 8), days))
days_dict_rev = dict(zip(days, range(1, 8)))
print('This is a days dictionary', days_dict)
print('This is a days dictionary from another Universe:', days_dict_rev)
