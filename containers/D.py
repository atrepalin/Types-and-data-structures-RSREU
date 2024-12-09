class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "error"

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return "error"

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()

while True:
    command = input().split()
    if command[0] == "push":
        queue.push(int(command[1]))
        print("ok")
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "clear":
        queue.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break
    else:
        print("error")
