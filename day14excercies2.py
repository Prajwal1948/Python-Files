def test():
    try:
        print("In try bloack")
        return 1
    except:
        print("In execept bloack")
    finally:
        print("In finally block")
        return 2

def main():
    print(test())

if __name__ == "__main__":
    main()