
def main():
    with open("Speach1day16.txt", 'r') as f:
        num_lines = 0
        num_words = 0

        for line in f:
            words = line.split()
            num_lines = num_lines + 1
            num_words = num_words + len(words)

    print(num_lines)
    print(num_words)

if __name__ == "__main__":
    main()