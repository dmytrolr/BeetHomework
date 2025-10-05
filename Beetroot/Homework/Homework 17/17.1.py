class Animal:
    def __init__(self, name: str = ""):
        self.name = name

    def talk(self):
        print("I am talking")


class Dog(Animal):
    def __init__(self, name: str = "Dog"):
        super().__init__(name)

    def talk(self):
        print(f"{self.name}: woof woof")


class Cat(Animal):
    def __init__(self, name: str = "Cat"):
        super().__init__(name)

    def talk(self):
        print(f"{self.name}: meow meow")


def make_talk(animal: Animal):
    """
    Викликає метод talk у екземпляра Animal (або підкласів).
    """
    animal.talk()


if __name__ == "__main__":
    big_dog = Dog("Beethoven")
    fat_cat = Cat("Garfield")

    make_talk(big_dog)
    make_talk(fat_cat)
