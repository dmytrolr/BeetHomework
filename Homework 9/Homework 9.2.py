import sys
print('\n'.join(sys.path)) # список директорій де Пайтон шукає модулі

# import module_a
# Тут отримуємо таку помилку:
#    import module_a
#    ModuleNotFoundError: No module named 'module_a'

# Спроба змінити шляхи пошуку
sys.path.append('/home/dmytro/Desktop/Python/Beetroot/Homework/Homework 9/Modules_9.1')  # ✅

# тестування

import module_a
print('\n'.join(sys.path))
# з'явилась адреса директорії з модулем
# /home/dmytro/Desktop/Python/Beetroot/Homework/Homework 9/Modules_9.1

print("module_a" in sys.modules) # результат True

#Так, sys.path можна змінити, але лише на час роботи з цими змінами.
# Якщо запускати скрипт з тієї ж директорії, де знаходиться mymod.py, то імпортувати можна без змін.
# Але якщо модуль лежить в іншій директорії, то або треба додати шлях до PYTHONPATH,
# або вставити цей шлях вручну в sys.path.
