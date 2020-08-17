def swap_case(s):
    my_list = []
    my_str = s.split()
    res = ''
    for string in s:
        for i in string:
            if i.isupper():
                res += i.lower()
            if i.isalpha() == False:
                res += i
            if i.islower():
                res += i.upper()
    my_list.append(res)
    string = ''
    for i in my_list:
        string += i
    return string
