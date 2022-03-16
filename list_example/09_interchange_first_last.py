# interchange first and last element in list:
list = eval(input('Enter first list: '))
a = list[0]
b = list[-1]
print('before interchange')
print(list)
for i in range(len(list)):
    list[0] = b
    list[-1] = a
print('after interchange')
print(list)