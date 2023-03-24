class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __floordiv__(self, other):
        return self.value // other.value

    def __divmod__(self, other):
        return self.value % other.value

    def __pow__(self, other):
        return self.value ** other.value

def main():
    number1 = Number (15)
    number2 = Number (2)
    print("Addition:", number1 + number2)
    print("Substraction:", number1 - number2)
    print("Multiplication:", number1 * number2)
    print("Division:", number1 / number2)
    #print("Division modulus:", number1 % number2)
    print("Power:", number1 ** number2)
    print("mod:", number1 % number2)
if __name__ == "__main__":
    main()