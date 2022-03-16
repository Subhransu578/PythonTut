# list = [10,20,25,30,40]
# print('missing value')
# for i in range(10,40,5):
#     if i not in list:
#         print(i)


list = eval(input('Enter a list: '))
for i in range(len(list)):
    if list[i] not in list:
        print(list[i])