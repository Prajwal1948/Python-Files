def main():
        try:
            num = int(input("Please Enter the number between range of 1 to 10: "))
            if num < 1 or num >10:
                raise ValueError("Number should be between 1 to 10")
            print(num)
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    main()