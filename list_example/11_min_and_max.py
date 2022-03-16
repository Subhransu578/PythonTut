# find min and max value from list:
list = eval(input("Enter a list: "))
print('**** Original List ****')
print(list)
lint = []
for i in list:
    if type(i) == int or type(i) == float:
        lint.append(i)
print('**** After filtered List ****')
print(lint)

min = max = lint[0]
for i in range(1,len(lint)):
    if min > lint[i]:
        min = lint[i]
    elif max < lint[i]:
        max = lint[i]
print(f'Min value is {min}')
print(f'Max value is {max}')