
def check_toys(function):
    def wrapper(toys, *args, **kwargs):
        if toys:
            return function(toys, *args, **kwargs)
        else:
            print("No toys play")
    return wrapper

def main():
    print(check_toys('xyz'))

if __name__=="__main__":
    main()