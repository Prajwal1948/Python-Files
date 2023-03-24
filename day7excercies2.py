class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def print_studnet_details(self):
        print("Student name and age is:", self.name, self.age)

class Marks(Student):
    def __init__(self, name, age, marks):
        super().__init__(name,age)
        self.marks=marks

    def print_studnet_marksdetails(self):
        print("Student name, age and marks is:", self.name, self.age, self.marks)

class Extraavtivity(Marks):
    def __init__(self, name, age, marks, activity):
        super().__init__(name,age, marks)
        self.activity=activity

    def print_studnet_activitydetails(self):
        print("Student name, age, marks and acitvity is:", self.name, self.age, self.marks, self.activity)

def main():
    s1 = Extraavtivity("Ram", 23, 78, "PT")
    s1.print_studnet_marksdetails()
    s1.print_studnet_details()
    s1.print_studnet_activitydetails()

if __name__ == "__main__":
    main()