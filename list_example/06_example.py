# create a list and replace int data with *
list = [10,20.3,'hello',20]
for i in range(len(list)):
    if type(list[i]) == int:
        list[i] = '*'
print(list)