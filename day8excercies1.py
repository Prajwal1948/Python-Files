class Shape:
    def __init__(self, height, width, shape_name):
        self.height = height
        self.width = width
        self. shape_name = shape_name

    def print_display_attributes(self):
        print("Shapes Attributes: ", self.height, self.width, self.shape_name)

class Reactangle(Shape):
    def __init__(self, height, width, shape_name):
        super().__init__(height, width, shape_name)

    def print_display_attributes(self):
        print("Rectangles Attributes: ", self.height, self.width, self.shape_name)

def main():
    shape = Shape(5.6, 6, "Square")
    reac = Reactangle(7, 4, "Reactangle")

    shape.print_display_attributes()
    reac.print_display_attributes()

if __name__ == "__main__":
    main()