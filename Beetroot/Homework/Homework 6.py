# 1
# Найбільше число
# Напишіть програму на мові Python для отримання найбільшого числа
# зі списку випадкових чисел довжиною 10.
# Обмеження: для генерації чисел використовувати тільки цикл while та модуль random
import random

nums = []
i = 0

while i < 10:
    nums.append(random.randint(1, 100))
    i += 1

large = max(nums)
print('Довжина списку:', len(nums))
print('Найбільше число зі списку:', large)

# 2
# Виключні спільні числа.
# Згенеруйте 2 списки довжиною 10 з випадковими цілими числами від 1 до 10,
# а також третій список, що містить спільні числа між двома
# початковими списками без повторень.
# Обмеження: для генерації чисел використовувати лише цикл while та модуль random

list_1 = []
list_2 = []
list_3 = []
i = 1

while (i <= 10):
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    i +=1

j = 0
while j < 10:
    if list_1[j] in list_2 and list_1[j] not in list_3:
        list_3.append(list_1[j])
    j += 1

print('First list:', list_1)
print('Second list:', list_2)
print('Only common values from both lists:', list_3)


#Завдання 3
# Вилучення чисел.
# Складіть список, який містить усі цілі числа від 1 до 100,
# потім знайдіть усі числа зі списку, які діляться на 7, але не кратні 5,
# і збережіть їх в окремому списку. Нарешті, виведіть список.
# Обмеження: для ітерації використовувати тільки цикл while.

list_hundredd = []
mod_list = []
i = 1

while i <= 100:
    list_hundredd.append(i)
    if i % 7 == 0 and i % 5 != 0:
        mod_list.append(i)
    i += 1

print('''All integers from the list that are divisible by 7, but 
not a multiple of 5:''', mod_list)


