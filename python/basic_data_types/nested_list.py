if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # print(students[1])

    name = [students[i][0] for i in range(len(students))]
    score = [students[i][1] for i in range(len(students))]

    print(students)
    print(name)
    my_sort = sorted(score, reverse=True)
    print(my_sort[len(my_sort)-2])
