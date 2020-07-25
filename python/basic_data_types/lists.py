if __name__ == '__main__':
    my_list = []
    N = int(input())
    for _ in range(N):
        command = input().strip().split(" ")
        if command[0] == 'insert':
            index = int(command[1])
            number = int(command[2])
            my_list.insert(index, number)
        elif command[0] == 'print':
            print(my_list)
        elif command[0] == 'remove':
            number = int(command[1])
            my_list.remove(number)
        elif command[0] == 'append':
            number = int(command[1])
            my_list.append(number)
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()
