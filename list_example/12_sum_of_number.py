# case-1:
# list = eval(input("Enter a list: "))
# print('**** Original list ****')
# print(list)
# sum = 0
# for i in range(len(list)):
#     sum = sum + list[i]
# print(f'Sum of numbers is {sum}')

# case-2:
list = eval(input("Enter a list: "))
print('**** Original list ****')
print(list)
list1 = []
for i in range(len(list)):
    if type(list[i]) == int:
        list1.append(list[i])
print('**** Only Integer list ****')
print(list1)
sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]
print(f'Sum of numbers is {sum}')