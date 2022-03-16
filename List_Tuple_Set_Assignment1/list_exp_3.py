# calculate distance between two points :
list = eval(input('Enter a list: '))
print('List is:')
for i in range(len(list)):
    print(f'Index {i} = {list[i]}')
print('Enter two element from list which you want the difference between them')
num1 = int(input('Enter 1st element index: '))
num2 = int(input('Enter 2nd element index: '))
print(f'Difference btn {num2} & {num1} index = {num2-num1}')
print(f'Difference btn {list[num2]} & {list[num1]} = {list[num2]-list[num1]}')