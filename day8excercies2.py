class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return 2 * self.length * self.breadth

class Reactangle(Shape):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def calculate_area(self):
        return super().calculate_area()

def main():
    reac = Shape(2, 3)
    shape = Reactangle(3,4)
    print(reac.calculate_area())
    print(shape.calculate_area())

if __name__ == "__main__":
    main()