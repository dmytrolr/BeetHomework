class Person:
    def __init__(self, name: str, surname: str, age: int, sex: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    def fullname(self):
        return f"{self.name} {self.surname}"

    def introduce(self):
        return f"Hello, my name is {self.fullname()}. I am {self.sex}, {self.age} years old."


class Student(Person):
    def __init__(
            self, name: str, surname: str, age: int, sex: str,
            group: str, course: int
    ):
        super().__init__(name, surname, age, sex)
        self.group = group
        self.course = course

    def study(self):
        return f" Student {self.fullname()} is studying in group {self.group} on course {self.course}."


class Teacher(Person):
    def __init__(
            self, name: str, surname: str, age: int, sex: str,
            subject: str, expirience: int, salary: float
    ):
        super().__init__(name, surname, age, sex)
        self.subject = subject
        self.expirience = expirience
        self.salary = salary

    def teach(self):
        return (f"Teacher {self.fullname()} teaches {self.subject} with {self.expirience}"
                f" years of experience and earns {self.salary} per month.")
