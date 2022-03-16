list = [10,20,25,30,40]
print('Original List')
print(list)
print('missing value')
for i in range(10,40,5):
    if i not in list:
        print(i)
print('After Add missing value')
for i in range(10,40,5):
    if i not in list:
        list.append(i)
list.sort()
print(list)