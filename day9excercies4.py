class Stack:
    def __init__(self):
        self.__stack_list = []

    def add_element(self, num):
        self.__stack_list.append(num)

    def remove_element(self):
        return self.__stack_list.pop()

    def display_elements(self):
        print(self.__stack_list)

def main():
    stack = Stack()
    stack.add_element(5)
    stack.add_element(3)
    stack.display_elements()
    stack.remove_element()
    stack.display_elements()

if __name__ == "__main__":
    main()