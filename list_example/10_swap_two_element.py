# swap two elements in list:
list = eval(input('Enter a list: '))
print('**** Before swap ****')
for i in range(len(list)):
    print(f'{list[i]} = {i} index')
pos1 = int(input('Enter first index you want to swap: '))
pos2 = int(input('Enter second index you want to swap: '))
temp = list[pos1]
list[pos1] = list[pos2]
list[pos2] = temp
print('**** After swap ****')
for i in range(len(list)):
    print(f'{list[i]} = {i} index')