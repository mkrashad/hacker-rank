if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    mylist = list()
    first = students[1][1]
    second = students[len(students)-1][1]
    for i in range(len(students)):
        if first > students[i][1]:
            second = first
            first = students[i][1]
        if students[i][1] < second and students[i][1] > first:
            second = students[i][1]
    mylist.append(second)


    result = list()
    for i in range(len(students)):
        if students[i][1] == mylist[0]:
            result.append(students[i][0])


    second = sorted(result)
    for i in second:
        print(i)
