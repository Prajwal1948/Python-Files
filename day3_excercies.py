class Vehicle:
    wheels = 4
    no_of_doors = 4

    def __init__(self, color, type, relaseyear):
        self.color = color
        self.type = type
        self.relaseyear = relaseyear

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return "Color changed"

    def describe_vehicle(self):
        print('The color of vehicle is', self.color, 'the type is', self.type, 'relased year is', self.relaseyear)

    def breake_car(self):
        print(self.describe_vehicle(), "breaking")

    def star_car(self):
        print("starting")


def main():
    v1 = Vehicle("black", "Mercedes", 1970)
    v1.describe_vehicle()
    v2 = Vehicle("Red", "Audi", 1980)
    v2.describe_vehicle()
    print(v1.set_color("blue"))
    print(v1.describe_vehicle())
    print(v2.star_car())
    print(v1.breake_car())


if __name__ == '__main__':
    main()
