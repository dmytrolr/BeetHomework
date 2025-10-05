# 1
# Проста функція.
#
# Створіть просту функцію з назвою favorite_movie, яка отримує на вхід рядок,
# що містить назву вашого улюбленого фільму.
# Функція повинна вивести "Мій улюблений фільм має назву {ім'я}".
def favorite_movie(name):
    print('My favorite movie is named', name)

favorite_movie('Капітошка')

#2
# Створення словника.
#
# Створіть функцію make_country, яка отримує назву країни та її столицю як параметри.
# Потім створіть словник на основі цих двох даних, з "назвою" як ключем і "столицею" як параметром.
# Зробіть так, щоб функція виводила значення словника, щоб переконатися, що вона працює належним чином.

def make_country(name, capital):
    country = {name: capital}
    return country

print(make_country('Ukraine', 'Kyiv'))

# Простий калькулятор.
#
# Створіть функцію make_operation, яка отримує простий арифметичний оператор
# як перший параметр (для спрощення нехай це буде лише '+', '-' або '*') і довільну
# кількість аргументів (лише числа) як другий параметр.
# Потім поверніть суму або добуток усіх чисел у довільному параметрі. Наприклад:
#
# виклик make_operation('+', 7, 7, 2) має повернути 16
# виклик make_operation('-', 5, 5, -10, -20) має повернути 30
# виклик make_operation('*', 7, 6) має повернути 42

def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        result = args[0]
        for arg in args[1:]: # Це мабуть найгірше і найкраще водночас. Як би я не назвав
            result -= arg    # елемент цього кортежу: хоч arg, хоч num - воно працює.
        return result        # І зручно, і водночас ця варіативність інколи дезорієнтує.
    elif operator == '*':
        result = 1
        for arg in args:
            result *= arg
        return result
#     else:
#         return 'Wrong operator'
print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
