# ex-1:
# def fun(l):
#     print(l)
# list = [1,2,3,4]
# fun(list)

# ex-2:
# def fun(l):
#     sum=0
#     for i in l:
#         sum = sum+i
#     print(f'sum of the list is {sum}')
# list=[1,2,3,4]
# fun(list)

# ex-3:
# def fun(l):
#     sum=0
#     for i in l:
#         sum = sum+i
#     print(f'sum of the list is {sum}')
# list=eval(input("Enter a list: "))
# fun(list)

# ex-4:
# list=['Ducati','Kawasaki','Honda','BMW']
# def search(l):
#     count=0
#     for i in l:
#         if i == brand:
#             print("Company found")
#             break
#         else:
#             count=1
#     if count == 1:
#         print("Company not found")
# brand = str(input("Search a company name: "))
# search(list)

# ex-5: join two list
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# def fun(l1,l2):
#     l1.extend(l2)
#     return l1
# print(fun(list1,list2))

# ex-6: add elements of two list
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list3=[]
# def fun(l1,l2):
#     if len(l1)==len(l2):
#         length=len(l1)
#         for i in range(length):
#             list3.append(l1[i]+l2[i])
#         return list3
#     else:
#         print("List length is not same")
# print(fun(list1,list2))

# ex-7: find max and min
list=eval(input('enter a list: '))
def minMax(l):
    min=max=l[0]
    for i in range(1,len(l)):
        if min>l[i]:
            min=l[i]
        elif max<l[i]:
            max=l[i]
    print(f'Min value = {min}\nMax value = {max}')
minMax(list)