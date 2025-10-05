# Напишіть функцію, яка приймає два числа від користувача за допомогою input(),
# називає ці числа a і b, а потім повертає значення квадрата a, поділеного на b.
# Створіть блок try-except, який виловлює виняток, якщо два значення, надані функцією input,
# не були числами, а значення b було нулем (не можна ділити на нуль).

def calculate(a: float, b: float) -> str:
    try:
        result = (a ** 2) / b
    except (ValueError, TypeError):
        return 'Неправильний тип даних! Вводьте лише числа!'
    except ZeroDivisionError:
        return 'Ділити на нуль не можна!'
    else:
        return f'Результат обчислень: {result}'


    # БЛОК ВИКЛЮЧЕНЬ
    except (ValueError, TypeError):
        print(
            'Неправильний тип даних!'
            ' Вводьте лише числа!'
        )
    except ZeroDivisionError:
        print(
            'Ділити на нуль не можна!'
        )
    else:
        print(
            'Результат обчислень: ', result
        )

calculate ()