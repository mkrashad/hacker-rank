if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    name = [students[i][0] for i in range(len(students))]
    score = [students[i][1] for i in range(len(students))]

    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]


    # second_lowest_names = []

    # second_lowest = sorted(score)
    # # first = students[0][1]
    # # second = students[0][1]
    # # lowest = []
    # for name, score in students:
    #     if score == second_lowest:
    #         second_lowest_names.append(name)
    # print(second_lowest_names)
            #     if first > score:
            #         first = score
            #     # if score < second and score > first:
            #     #     second = score
            #     lowest.append(name)
            # print(lowest)

            # first = students[0][1]
            # second = students[0][1]
            # name = students[4][0]
            # lowest = []
            # for i in students:
            #     if first > i[1]:
            #         second = first
            #         first = i[1]
            #     if i[1] < second and i[1] > first:
            #         second = i[1]
            # lowest.append(second)
            # # lowest.append(first)
            # # print(lowest)
            # print(lowest)
            # first = score[0]
            # second = score[0]
            # for i in score:
            #     if first > i:
            #         second = first
            #         first = i
            #     if i > second and i < first:
            #         second = i
            # print(second)
