class Queue:
    def __init__(self):
        self.__queue_list=[]

    def add_element_at_end(self, num):
        self.__queue_list.append(num)

    def add_element_at_start(self, num):
        self.__queue_list.insert(0, num)

    def remove_element_at_first(self):
        return self.__queue_list.pop(0)

    def remove_element_at_last(self):
        return self.__queue_list.pop(-1)

    def print_elements(self):
        print(self.__queue_list)

def main():
    queue = Queue()
    queue.add_element_at_start(5)
    queue.add_element_at_end(4)
    queue.add_element_at_start(6)
    queue.print_elements()
    print(queue.remove_element_at_last())
    print(queue.remove_element_at_first())
    queue.print_elements()

if __name__ == "__main__":
    main()