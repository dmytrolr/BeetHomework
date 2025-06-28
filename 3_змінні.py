print('Task_1')
print()
name = 'Stepan'
day = 'Saturday'
print('# concatenation')
message_1 = 'Good day ' + name + '! ' + day + ' is a perfect day to learn some python.'
print(message_1)
print('# .format')
message_2 = 'Good day {}! {} is a perfect day to learn some python.'.format(name, day)
print(message_2)
print('# f-strings')
message_3 = f'Good day {name}! {day} is a perfect day to learn some python.'
print(message_3)
print()
print('# Task_2')
print('# Using separate variables with concatentation strings')
name_1='Dmytro'
surname_1='Kaduk'
message_3='Hello, '+ name_1 + ' ' + surname_1 + ', have a great day!'
print(message_3)
print()
print('# Task_3')
a=14
b=5
print(f'a={a},b={b}')
print()
# a+b=14+5=19
print(f'a+b=14+5={a+b}')
print()
# a-b=14-5=9
print(f'a-b=14-5={a-b}')
print()
# a:b=14:5=2.8
print(f'a:b=14:5={a/b}')
print()
# axb=14x5=70
print(f'axb=14x5={a*b}')
print()
#(axb)^2=(14x5)^2=4900
print(f'(axb)^2=(14x5)^2={(a*b)**2}')
print('# or using two additional variables for showing intermediate result')
#(14x5)^2 = 70^2 = 4900
product = a*b
square = product**2
print(f'({a}x{b})^2={product}^2={square}')
print()
print("""# Using modulus: a%b=14%5=4, because function modulus will return remainder from modulus operation. As you know
 maximum multiplication for 5 in 14 range is 2, so: 14-(5x2)=4""")
print(f'a%b={a}%{b}={a%b}')
print()
print("""# Using floor division: a//b=14//5=2; Since 14 ÷ 5 = 2.8, we discard the fractional part and get the result 2""")
print(f'a//b={a}//{b}={a//b}')
print()
print("""Післямова
         В даному завданні я продемонстрував методи роботи з рядками і змінними. 
         Особисто мені найзручнішим і найпрактичнішим здається метод f-strings, хоча я досі не впевнений в його універсальності.
         Також намагався найзрозуміліше відобразити результати роботи кода для споживача. Можливо десь зайве, 
         а можливо і ні. Потрібна твоя думка стосовно такої реалізації.
         Буду вдячний за коментарі.""")