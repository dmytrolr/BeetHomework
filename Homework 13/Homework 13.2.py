# Напишіть програму на Python для доступу до функції всередині функції
# (Поради: використовуйте функцію, яка повертає іншу функцію)

def outer_function():
    def inner_function():
        print("I`m from inner function")

    return inner_function


f = outer_function()
f()
