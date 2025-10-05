# ЗНам потрібна функція, яка може перетворити число (ціле число) у рядок.
#
# Які способи досягнення цього ви знаєте?
# Приклади (ввід --> вивід):
#
# 123 --> "123"
# 999 --> "999"
# -100 --> "-100"

# def number_to_string(num):
#     return str(num)

# Дезоксирибонуклеїнова кислота (ДНК) - це хімічна речовина, що міститься в ядрі клітин і несе в собі
# "інструкції" для розвитку та функціонування живих організмів.
# Якщо ви хочете дізнатися більше: http://en.wikipedia.org/wiki/DNA
# У ланцюжках ДНК символи "А" і "Т" доповнюють один одного, як "Ц" і "Г". Ваша функція отримує одну
# сторону ДНК (рядок, за винятком Haskell); вам потрібно повернути іншу комплементарну сторону.
# Нитка ДНК ніколи не буває порожньою або взагалі відсутня (знову ж таки, за винятком Хаскела).
# Більше подібних вправ можна знайти тут: http://rosalind.info/problems/list-view/ (джерело)
# Приклад: (вхід --> вихід)
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def DNA_strand(dna):
    DNA = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(DNA[nucleotide] for nucleotide in dna)


print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))


# и, мабуть, знаєте кілька досить великих ідеальних квадратів.
# Але як щодо наступного? Допишіть метод findNextSquare,
# який знаходить наступний за переданим у якості параметра і
# нтегральний досконалий квадрат.
# Нагадаємо, що цілим досконалим квадратом називається
# таке ціле число n, що sqrt(n) також є цілим числом.
# Якщо аргумент сам по собі не є досконалим квадратом, то
# повертається або -1, або пусте значення типу
# None або null, залежно від вашої мови.
# Ви можете вважати, що аргумент невід'ємний.
# Приклади ( Вхідні дані --> Вихідні дані ) 121 --> 144
# 625 --> 676
# 114 --> -1 # оскільки 114 не є досконалим квадратом
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    else:
        return -1


# Тролі атакують ваш розділ коментарів!
# Звичайний спосіб впоратися з цією ситуацією - видалити всі голосні з коментарів тролів, нейтралізувавши таким чином загрозу.
# Ваше завдання - написати функцію, яка отримує на вхід рядок і повертає новий рядок з видаленими голосними.
# Наприклад, рядок "This website is for losers LOL!" перетвориться на "Ths wbst s fr lsrs LL!".
# Зауважте: у цій каталозі y не вважається голосною.

def disemvowel(string_):
    result = string_.translate(string_.maketrans('', '', 'aeiouAEIOU'))
    return result


# Об'єднання речень
# # Напишіть функцію, яка отримує масив слів, об'єднує їх у речення і повертає речення. Ви можете ігнорувати будь-яку
# потребу в очищенні слів або додаванні розділових знаків, але ви повинні додати пробіли між кожним словом.
# Будьте уважні, пробілу не повинно бути ні на початку, ні в кінці речення!
# Приклад
#  ['hello', 'world', 'this', 'is', 'great'] => 'hello world this is great'
# # Припущення
#    Ви можете вважати, що вам задано лише слова.
#    Розмір масиву не може бути задано.
#    Можна вважати, що ви отримуєте масив.
# # Що ми тестуємо
#  Ми тестуємо базові цикли та маніпуляції з рядками. Він призначений для початківців, які тільки вивчають цикли
#  та маніпуляції з рядками.
# Dдмова від відповідальності
#  Цей тест призначений для початківців, тому ми хочемо протестувати базові цикли та маніпуляції з рядками.
#  Досвідчені користувачі зможуть легко зробити це в одному рядку.
def smash(words):
    sentence = " ".join(words)
    return sentence


# Опис:
# Повернути кількість (лічильник) голосних у заданому рядку.
# Будемо вважати a, e, i, o, u голосними для цієї Ката (але не y).
# Вхідний рядок складається лише з малих літер та/або пропусків.
def get_count(sentence):
    count = 0
    for ch in sentence:
        if ch in 'aeiou':
            count += 1
    return count


# Create a function that accepts a parameter representing a name and returns the message: "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]
def greet(name):
    return f"Hello, {name} how are you doing today?"


# За заданим списком цілих чисел визначте, чи є сума його елементів непарною або парною.
# Відповідь виведіть у вигляді рядка, що відповідає "непарна" або "парна".
# Якщо вхідний масив порожній, то вважати його як: [0] (масив з нулем).
# Приклади:
# Вхідні дані: [0]
# Вихідні дані: "even"
# Вхідні дані: [0, 1, 4]
# Output: "непарне"
# Вхідні дані: [0, -1, -5]
# Вихідні дані: "парне"
def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"

    # def oddOrEven(arr):
    #     return 'even' if sum(arr) % 2 == 0 else 'odd'
    # Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
    # Examples:
    # solution('abc', 'bc') # returns true
    # solution('abc', 'd') # returns false
    # def solution(string, ending):
    #    return True if string.endswith(ending) else False

    # Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
    # For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1. (81-1-1-81)
    # Example #2: An input of 765 will/should return 493625 because 7**2 is 49, 6**2 is 36, and 5**2 is 25. (49-36-25)
    # Note: The function accepts an integer and returns an integer.
    # Happy Coding!
    # def square_digits(num):
    result = ('')
    for i in str(num):
        result += str(int(i) ** 2)
    return int(result)

    return int(''.join(str(int(i) ** 2) for i in str(num)))
