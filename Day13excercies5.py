
def absSum(function):
    def wrapper(x, y):
        result = function(x, y)
        return abs(result)
    return wrapper

def addNum(x, y):
    return x + y

def main():
    result = addNum(5, 10)
    print(result)

if __name__=="__main__":
    main()