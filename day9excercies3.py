class Employee:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def print_attributes(self):
        print("Employee sttributes are:", self.name, self.age, self.id)

    def display_qualification(self):
        print('qualification:',self.qualification)


class Person(Employee):
    def __init__(self, qualification):
        super().__init__(qualification)

    def print_attributes(self):
        print("Person qualification:",self.qualification)

def main():
    person = Person('MSC')
    emp = Employee("Ram", 23, 1223)
    person.print_attributes()
    emp.display_qualification()

if __name__ == "__main__":
    main()