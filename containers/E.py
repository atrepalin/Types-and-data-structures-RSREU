class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, item):
        self.items.insert(0, item)
        print("ok")

    def push_back(self, item):
        self.items.append(item)
        print("ok")

    def pop_front(self):
        if self.items:
            print(self.items.pop(0))
        else:
            print("error")

    def pop_back(self):
        if self.items:
            print(self.items.pop())
        else:
            print("error")

    def front(self):
        if self.items:
            print(self.items[0])
        else:
            print("error")

    def back(self):
        if self.items:
            print(self.items[-1])
        else:
            print("error")

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print("ok")

    def __bool__(self):
        return bool(self.items)


deque = Deque()

while True:
    command = input().split()
    if command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "pop_front":
        deque.pop_front()
    elif command[0] == "pop_back":
        deque.pop_back()
    elif command[0] == "front":
        deque.front()
    elif command[0] == "back":
        deque.back()
    elif command[0] == "size":
        deque.size()
    elif command[0] == "clear":
        deque.clear()
    elif command[0] == "exit":
        print("bye")
        break
    else:
        print("error")