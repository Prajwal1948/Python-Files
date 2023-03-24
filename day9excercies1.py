class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_hello(self):
        print("Hello ", self.name)


class Marks:
    def __init__(self, marks):
        self.subject = subject

    def print_subject(self):
        print("Subject ", self.subject)

def main():
    s1 = Student("Ram", 23)
    m1 = Marks(45)
    s1.print_hello()
    m1.print_subject()


if __name__ == "__main__":
    main()
