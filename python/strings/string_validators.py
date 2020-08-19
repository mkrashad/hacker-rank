if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = False
    for i in s:
        if i.isalnum():
            alnum = i.isalnum()
        if i.isalpha():
            alpha = i.isalpha()
        if i.isdigit():
            digit = i.isdigit()
        if i.islower():
            lower = i.islower()
        if i.isupper():
            upper = i.isupper()
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
