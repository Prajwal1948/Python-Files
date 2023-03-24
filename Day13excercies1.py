def prime_numbers():
    for num in range(1, 5000):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    print(num)
def main():
    p = prime_numbers()

if __name__ == "__main__":
    main()
