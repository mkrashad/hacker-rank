class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):

        return self.stack.pop()

    def get_value(self):
        return self.stack


my_stack = Stack()
max_elem = 0

for i in my_stack.get_value():
    print(i)

for _ in range(int(input())):
    n = list(map(int, input().strip().split()))
    command = int(n[0])
    if command == 1:
        max_elem = max(max_elem, n[1])
        my_stack.push(n[1])
    elif command == 2:
        if my_stack.pop() == max_elem:
            if len(my_stack.get_value()) > 0:
                max_elem = max(my_stack.get_value())
            else:
                max_elem = 0
    elif command == 3:
        print(max_elem)
