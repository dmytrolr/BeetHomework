age = 20
if age < 18:
    print("Ти ще дитина.")
elif age < 60:
    print("Дорослий.")
else:
    print("Пенсіонер.")


name = "Olga"
if name.startswith('O'):
    print('Привіт, Оля!')
else: print('Привіт, незнайомцю!')

#1
score = int(input("Введи оцінку: "))
if len(score) <4:
    print('SHORT NAME')
elif len(score) >6:
    print ('LONG NAME')
else:
    print('OK')

#2
score = int(input("Введи оцінку: "))
if score <60:
    print('BAD!')
elif score [60:80]:
    print('NOT BAD')
elif score [81:90]:
    print('VERY GOOD')
else: print('EXCELLENT!')

#3
#1
# Введи вік і місто. Якщо вік понад 18 і місто — "Kyiv", надрукуй "Вітаємо!"
# Інакше — "Доступ заборонено"
if (age > 18 and city==Kyiv):
    print('Вітаємо')
else:
    print('Доступ заборонено!')

#2
# username має дорівнювати "admin", а password — "12345"
# Якщо все збігається, надрукуй "Успішний вхід"
# Інакше — "Помилка входу"
username = int(input(""))
password = int(input(""))
if (username='admin' and password='12345'):
    print('Успішний вхід')
else:
    print('Помилка входу')

#3
# Ім’я повинно бути або "Olga", або "Olya"
# Якщо це так, виведи "Привіт, Олю!"
# Інакше — "Привіт, незнайомцю"
name = int(input("Введи: "))
name = "Olga" or "Olya"
if (name=='Olga' or name=='Olya'):
    print('Привіт, Оля!')
else: print('Привіт, незнайомцю!')

#4
# Запитай у користувача число
# Якщо воно в межах від 10 до 20 (включно) — надрукуй "У межах"
# Інакше — "Поза межами"
numbescore = int(input("Input number"))
if 10 <= numberscore <= 80:
    print('In range')
else:
    print('Out of range')

#5
# Запитай у користувача текст
# Якщо рядок не пустий, надрукуй "Дякую!"
# Інакше — "Рядок порожній"
text_1= input('Enter text')
if (len(text_1)==1<=):
    print('Ok')
else:
    print('Empty string')

