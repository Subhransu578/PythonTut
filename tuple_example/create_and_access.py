# ex-1:
# t=(12,3,2)
# print(t)
# print(type(t))

# ex-2:
# t=12,3,2
# print(t)
# print(type(t))

# ex-3:
# t=(12)
# print(t)
# print(type(t))

# it show int type, to avoid this we use ,
# ex-4:
# t=(12,)
# print(t)
# print(type(t))

# ex-5: using tuple() function
# list = [12,3,2,4]
# t = tuple(list)
# print(t)

# ex-6: using range()
# t = tuple(range(10,20,2))
# print(t)

# ex-7: using index access the element of tuple
# t = (1,3,2,5,7)
# print(t[0])
# print(t[-1])
# print(t[150])

# ex-8: using slice operator access the element of tuple
# t = (1,3,2,5,7)
# print(t[1:4])
# print(t[::2])

# ex-9: we can not update tuple element
# t=(10,20,30,40,50)
# t[1]=70
# print(t)

# ex-10: + operator is used to concatinate more than two tuple
# t1 = (1,2,3,4)
# t2 = (5,6,7,8)
# t3 = t1+t2
# print(t3)

# ex-11: 
# t1 = (1,2,3,4)
# t3 = t1*3
# print(t3)

# TypeError: can't multiply sequence by non-int of type 'tuple'
t1 = (1,2)
t2 = (5,6)
t3 = t1*t2
print(t3)