# Працівник має властивість "бос", і його значенням має бути екземпляр Боса.
# Ви можете перепризначити це значення, але ви повинні перевірити, чи є нове значення босом.
# Кожен бос має список своїх робітників. Ви повинні реалізувати метод, який дозволяє додавати робітників до боса.
# Вам не дозволяється додавати екземпляри класу Boss до списку робітників безпосередньо через доступ до атрибуту,
# замість цього використовуйте гетери та сетери!
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker: 'Worker'):
        if isinstance(worker, Worker):
            if worker is not self._workers:
                self._workers.append(worker)
                worker.boss = self
        else:
            raise TypeError("Worker must be an instance of Worker class.")

    def get_workers(self):
        return self._workers.copy()  # довелось використовувати .copy() щоб користувач отримував доступ не напряму


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss = None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        if boss is not None:
            self.boss = boss  # for setter using

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            if self not in new_boss.get_workers():
                new_boss.add_worker(self)
        else:
            raise TypeError("Boss must be an instance of Boss class.")


# boss making
boss1 = Boss(1, "Олег", "TechCorp")
boss2 = Boss(2, "Ірина", "InnoSoft")

# workers making
worker1 = Worker(101, "Андрій", "TechCorp", boss1)
worker2 = Worker(102, "Марія", "TechCorp")
worker3 = Worker(103, "Сергій", "InnoSoft")

# check how worker glued to boss
print("Робітники Олега:", [w.name for w in boss1.get_workers()])

# adding worker2 to boss1
boss1.add_worker(worker2)
print("Робітники Олега:", [w.name for w in boss1.get_workers()])

worker3.boss = boss2
print("Робітники Ірини:", [w.name for w in boss2.get_workers()])

print("Бос Марії:", worker2.boss.name)
