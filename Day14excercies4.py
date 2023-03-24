def Division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Division by 0')
    except ValueError:
        print('invalid input')
    except Exception as e:
        print('error of e')
    else:
        return result

def main():
    result = Division(4, 2)
    result = Division(5, 0)
    result = Division('4', 2)
    result = Division(2, 'a')
    print(result)

if __name__ == "__main__":
    main()