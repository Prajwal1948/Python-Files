class Student:
    def __init__(self, age, name, subject=['maths','hindi','sci'], marks=[65,60,41]):
        self.age = age
        self.name = name
        self.subject = subject
        self.marks = marks

    def __mul__(self, other):
        for idx,sub in enumerate(self.marks):
            if(self.marks[idx]>other.pass_marks[idx]):
                continue
            else:
                return "failed"
        return "pass"
class Exams:
     def __init__(self, subject=['match','hindi','sci'], pass_marks=[35,40,40]):
        self.subject = subject
        self.pass_marks = pass_marks

def main():
    s=Student(24,'Ram')
    E=Exams()
    print(s * E)

if __name__=="__main__":
    main()