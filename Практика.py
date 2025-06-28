word = input("Введи слово: ")
if word == "hello":
    print("Ти сказав привіт!")
else:
    print('Ти не привітався')
#
age = int(input("Введи свій вік: "))
if age > 18:
    print("Ти дорослий!")
#
chs=int(input("Додай число: "))
if chs > 10:
    print("OK")
else:
    print("Too small")
#
word_2=input("Напиши одне слово: ")
if word_2 == "python":
    print("COOL")
else:
    print("Спробуй ще раз")
#
#
liko=input("Напиши щось: ")
calk=('п')
count = 0
for ch in liko.lower():
    if ch in calk:
        count += 1
print('Кількість літер "п":', count)

#1
num=int(input("додай число: "))
if num%2==0:
    print("Even")
else:
    print("Odd")
#2
ling=input("Введи текст: ")
ondo="аеєиіїоуюя"
for ch in ling.lower():
    if ch in ondo:
        print(ch, sep=', ')
#3


#4
sentence=input("<UNK> <UNK>: ")
beta='и'
count = 0
for ch in sentence.lower():
    if ch in beta:
        count += 1
print('Кількість літер "и":', count)

#В циклі while задайте умову для проходження змінної my_number від 1 до 25
# (при кожному проході виводьте на прінт значення my_number),
# але зупиніть виконання коли my_number буде ділитись без остачі на 3 і на 7.

#Запитай у користувача рядок. Порахуй, скільки в ньому голосних (а, е, є, и, і, ї, о, у, ю, я), і виведи їхню кількість.
sentence_1=input("Напиши щось: ")
volare='аеєиіоюяї'
count=0
for ch in sentence_1.lower():
    if ch in volare:
       count += 1
print(count, ' голосних літер')

#Задача 2: Вивести числа від 1 до 20, крім тих, що кратні 3 або 5
for ch in range(1, 21):
    if ch % 3 == 0 or ch % 5 == 0:
        continue
    print(ch, end=' ')