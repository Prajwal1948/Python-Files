class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("animal can't speak")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

def main():
    mydog = Dog("King")
    mycar = Car("TATA", "Nano")

    print(isinstance(mydog, Animal))
    print(isinstance(mycar, Animal))
    print(isinstance(mycar, Car))

    print(isinstance(Dog, Animal))
    print(isinstance(Car, Animal))
    print(isinstance(Car, object))

if __name__ == "__main__":
    main()

