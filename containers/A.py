class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "error"

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "error"

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def is_empty(self):
        return not self.items


stack = Stack()

while True:
    command = input().split()
    if command[0] == "push":
        stack.push(int(command[1]))
        print("ok")
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "back":
        print(stack.back())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "clear":
        stack.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break
    else:
        print("error")
