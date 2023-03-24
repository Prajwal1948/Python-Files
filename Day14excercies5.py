def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print(result)
    finally:
        print("This message always be printed, regardless of wether the exception was raised or not.")

def main():
    print(division(2, 4))

if __name__ =="__main__":
    main()