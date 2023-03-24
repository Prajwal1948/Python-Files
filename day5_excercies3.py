from multipledispatch import dispatch
class Calculator:

    def __int__(self,num1,num2,num3=1):
        self.num1=num1
        self.num2=num2
        self.num3=num3

    @dispatch(int,int)
    def add_two_numbers(self,num1,num2):
        return num1 + num2

    @dispatch(int,int,int)
    def add_three_numbers(self, num1, num2,num3):
        return num1 + num2 + num3

    @dispatch(int,int)
    def substract_two_number(self,num1,num2):
        return num1 - num2

    @dispatch(int,int,int)
    def substract_three_number(self,num1,num2,num3):
        return num1 - num2 - num3

def main():
    my_cal=Calculator()
    result = my_cal.substract_three_number(2,3,6)
    print(result)
    #result1 = my

if __name__=="__main__":
    main()