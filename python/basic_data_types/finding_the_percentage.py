if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = 0
    length = len(student_marks[query_name])
    for j in student_marks[query_name]:
        average = j + average
    avg = average / length
    print('{:.2f}'.format(avg))
