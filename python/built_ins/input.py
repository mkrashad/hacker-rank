if __name__ == '__main__':
    x, k = input().split()
    x = int(x)
    k = int(k)
    P = input()
    evaluated = eval(P)
    if evaluated == k:
        print(True)
    else:
        print(False)
