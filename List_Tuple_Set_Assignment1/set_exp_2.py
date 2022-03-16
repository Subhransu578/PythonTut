# element present in another set or not:
s1 = eval(input('Enter element of set1: '))
s2 = eval(input('Enter element of set2: '))
sl1 = list(s1)
sl2 = list(s2)
for i in range(len(sl1)):
    if sl1[i] in sl2:
        print(sl1[i])