# 1: create a list which is divisible by 10 and 5
# list = [10,20,35,27,43]
# print(list)
# for i in list:
#     if i%10==0 and i%5==0:
#         print(f'{i} is divisible')


# 2: create a list which is not divisible by 10 and 5
# list = [10,20,30,27,43]
# print(list)
# for i in list:
#     if i%10!=0 and i%5!=0:
#         print(f'{i} is not divisible')


# 3: create a list with different type of value and display value and its type
# list = [10,20.3,'hello',20]
# for i in list:
#     if type(i) == int:
#         print(f'{i} is int type')
#     elif type(i) == float:
#         print(f'{i} is float type')
#     elif type(i) == str:
#         print(f'{i} is string type')


# 4: check how many int, string, float value are present in your list
# list = [10,20.3,'hello',20]
# count1 = 0
# count2 = 0
# count3 = 0
# for i in list:
#     if type(i) == int:
#         count1 += 1
#     elif type(i) == str:
#         count2 += 1
#     elif type(i) == float:
#         count3 += 1
# print(f'int is {count1} time')
# print(f'str is {count2} time')
# print(f'float is {count3} time')


# 5: display list element by using positive and negative index
list = [10,20.3,'hello',20]
i = 0
j = 0
while i < len(list):
    print(f'{list[i]} is in {i} or {j} index')
    print()


# 6: create a list and replace int data with *
# list = [10,20.3,'hello',20]
# for i in range(len(list)):
#     if type(list[i]) == int:
#         list[i] = '*'
# print(list)