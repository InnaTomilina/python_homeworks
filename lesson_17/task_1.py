class Animal:
    def talk(self):
        raise Exception("Method has no implementation")


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def speak_with(animal: Animal):
    animal.talk()


dog = Dog()
cat = Cat()

speak_with(dog)
speak_with(cat)