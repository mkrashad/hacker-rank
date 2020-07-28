def miniMaxSum(arr):
    my_list = []
    result1 = 0
    result2 = 0
    arr1 = [i for i in arr]
    arr2 = [i for i in arr]
    exc_max = max(arr1)
    exc_min = min(arr2)
    arr1.remove(exc_max)
    arr2.remove(exc_min)
    for i in arr1:
        result1 += i
    for i in arr2:
        result2 += i
    print(str(result1) + " " + str(result2))

