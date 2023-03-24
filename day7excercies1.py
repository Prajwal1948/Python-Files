class Student:
    def __init__(self, name):
        self.name=name

    def print_Student_name(self):
        print(self.name)

class Exam(Student):
    def __init__(self, name,marks):
        super().__init__(name)
        self.marks=marks

    def print_Student_marks(self):
        print(self.marks)

def main():
    s1 = Exam("Ram", 67)
    s1.print_Student_name()
    s1.print_Student_marks()

if __name__ == "__main__":
    main()