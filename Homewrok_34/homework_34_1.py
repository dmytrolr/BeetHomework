import threading

counter = 0
rounds = 100_000

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            counter += 1

# Запускаю 99 разів
for i in range(1, 100):
    counter = 0
    t1 = Counter()
    t2 = Counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Запуск {i}: результат = {counter}")


# у мене результат кожного разу 200000