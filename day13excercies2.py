def my_names(names):
    for name in names:
        print(name)
    print("\n")
    for name in names:
        print (name.strip().title())

def main():
    n = ["rick", "Morty","beth","Summer","jerRy"]
    my_names(n)

if __name__ == "__main__":
    main()