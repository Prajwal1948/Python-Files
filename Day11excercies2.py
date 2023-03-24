from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def has_animal(self):
        pass

    @abstractmethod
    def has_attributes(self):
        pass

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound

    def has_animal(self):
        print("this is cat")

    def has_attributes(self):
        print("Sound is :", self.sound)

class Dog(Animal):
    def __init__(self, num_of_legs):
        self.num_of_legs = num_of_legs

    def has_animal(self):
        print("this is dog")

    def has_attributes(self):
        print("num of legs are: ", self.num_of_legs)

class Tiger(Animal):
    def __init__(self, tail):
        self.tail = tail

    def has_animal(self):
        print("this is tiger")

    def has_attributes(self):
        print("has tail", self.tail)

def main():
    tiger = Tiger(True)
    tiger.has_animal()
    tiger.has_attributes()

    cat = Cat("high")
    cat.has_attributes()
    cat.has_animal()

    dog = Dog(4)
    dog.has_animal()
    dog.has_attributes()

if __name__ == "__main__":
    main()