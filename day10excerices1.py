class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print("I am mammal")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print("I am Dog")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print("I am cat")

def main():
    mammal =Mammal("XYZ")
    dog = Dog("King")
    cat = Cat("ABC")

    dog.speak()
    mammal.speak()
    cat.speak()

if __name__ == "__main__":
    main()
