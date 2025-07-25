# Напишіть програму на мові Python для визначення кількості локальних змінних, оголошених у функції.

def count_locals():
    def stupid_task():
        a = 4
        b = 6
        c = -3
        d = a + b + c
        return d

    # Викликаю атрибут .__code__
    # print(dir(stupid_task.__code__))
    # в списку є кілька атрибутів для виконання завдання
    #  .co_varnames - кортеж з іменами усіїх змінних. В принципі, задачу можна вирішити і через нього:

    # def count_locals():
    #     def stupid_task():
    #         a = 4
    #         b = 6
    #         c = -3
    #         d = a + b + c
    #         return d
    #
    #     return len(stupid_task.__code__.co_varnames)
    # print(count_locals())  # Вивід: 4

    # Але мені більше подобається варіант вирішення через .co_nlocals,
    # хоча ім'я цього атрибута ніяк не натякає на те, що він в собі містить.

    return stupid_task.__code__.co_nlocals


print(count_locals())  # Вивід: 4
