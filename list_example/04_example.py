# check how many int, string, float value are present in your list
list = [10,20.3,'hello',20]
count1 = 0
count2 = 0
count3 = 0
for i in list:
    if type(i) == int:
        count1 += 1
    elif type(i) == str:
        count2 += 1
    elif type(i) == float:
        count3 += 1
print(f'int is {count1} time')
print(f'str is {count2} time')
print(f'float is {count3} time')