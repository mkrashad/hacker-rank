if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
