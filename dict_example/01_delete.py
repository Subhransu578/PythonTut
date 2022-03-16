# by using del:
# ex-1:
# d={1:'ducati',2:'kawasaki',3:'honda'}
# del d[3]
# print(d)

# ex-2:
# d={1:'ducati',2:'kawasaki',3:'honda'}
# del d[4]
# print(d)

# ex-3:
d={1:'ducati',2:'kawasaki',3:'honda'}
print(d)
del d
print(d) # NameError: name 'd' is not defined

# by using clear():
# d={1:'ducati',2:'kawasaki',3:'honda'}
# print(d)
# d.clear()
# print(d)