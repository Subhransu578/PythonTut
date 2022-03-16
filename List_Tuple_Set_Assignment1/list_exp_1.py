# Remove empty list from list
list1 = eval(input('Enter a list: '))
print('Before remove')
print(list1)
for i in list1:
    if type(i) == list:
        list1.remove(i)
print('After remove')
print(list1)