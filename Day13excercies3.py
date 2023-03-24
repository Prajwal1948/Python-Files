
def printer(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result is not None:
            print(result)
        return result
    return wrapper

def my_func(x, y):
    return x + y

def main():
    result = my_func(4, 5)
    print(result)

if __name__ == "__main__":
    main()