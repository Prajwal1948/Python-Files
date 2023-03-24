class Student:
    """"
    This is for studetn class
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_attributes(self):
        print("student attributes are:", self.name, self.age)

    def __repr__(self):
        return "Student Repr:" + self.name + str(self.age)

def main():
    s1 = Student("Ram", 23)
    print(dir(s1))
    print(id(s1))
    print(type(s1))
    print(Student.__doc__)
    print(Student.__name__)
    print(hasattr(s1, "print_student_attributes"))
    print(getattr(s1, "name"))
    print(repr(s1))
    s1.print_student_attributes()

if __name__ == "__main__":
    main()