# Task 1

s = input('Write a few words, my friend: ')
# Встановлюю умови для роботи з довжиною рядка,
# використовую індекси для зрізів.
if len(s) >=2:
    result = s[:2] + s[-2:]
else:
    result = ' '
print(result)


#2
while True:
    phone_numb = input('Write a phone number (only 10 digits): ')
# making conditions for identification correct phone number
    if phone_numb.isdigit()and len(phone_numb)==10:
        print('Thank you!')
        # finish cycle, if phone number is correct
        break
    else:
        print('That is not a valid phone number!')


#3
while True:
    answer = input('Скільки буде 11х3? Введи відповідь сюди: ')
    if answer.isdigit() and int(answer) == 33:
        print('Це правильна відповідь.')
        break
    else:
        print(' Помилка, старайся краще!')


#4
based_name = 'Дмитро'
user_name = input("Напиши своє ім'я тут: ")
if user_name.lower() == based_name.lower():
    print('True')
else:
    print('False')
