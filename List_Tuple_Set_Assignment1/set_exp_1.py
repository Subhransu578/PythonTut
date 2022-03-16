# Max and min in set:
s = eval(input('Enter a set: '))
print(s)
s1 = list(s)
max = min = s1[0]
for i in range(len(s1)):
    if max < s1[i]:
        max = s1[i]
    if min > s1[i]:
        min = s1[i]
print('max =',max)
print('min =',min)