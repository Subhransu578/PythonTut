list = eval(input('Enter a list: '))
diffmax = list[-1] - list[0]
diffmin = list[-1] - list[0]
max1 = max2 = min1 = min2 = list[0]
for i in range(len(list)):
    j = len(list) - 1
    while j>=0:
        if list[j] > list[i]:
            if diffmax < (list[j] - list[i]):
                diffmax = list[j] - list[i]
                max1 = list[j]
                min1 = list[i]
        else:
            if diffmax < (list[i] - list[j]):
                diffmax = list[i] - list[j]
                max1 = list[j]
                min1 = list[i]
        j = j-1
print(f'Large difference is {diffmax} between {max1} and {min1} number')

for i in range(len(list)):
    j = len(list) - 1
    while j>i:
        if list[j] > list[i]:
            if diffmin > (list[j] - list[i]):
                diffmin = list[j] - list[i]
                max2 = list[j]
                min2 = list[i]
        else:
            if diffmin > (list[i] - list[j]):
                diffmin = list[i] - list[j]
                max2 = list[j]
                min2 = list[i]
        j = j-1
print(f'Small difference is {diffmin} between {max2} and {min2} number')