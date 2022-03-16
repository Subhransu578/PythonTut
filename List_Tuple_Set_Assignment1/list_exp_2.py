# Remove duplicate from a list :

# 1st method:
# lst = eval(input('Enter a list: '))
# print('Before Remove')
# print(lst)
# lst1 = []
# for i in range(len(lst)):
#     if lst[i] not in lst1:
#         lst1.append(lst[i])
# print('After Remove')
# print(lst1)

# 2nd method:
lst = eval(input('Enter a list: '))
print('Before Remove')
print(lst)
lst = list(set(lst))
print('After Remove')
print(lst)