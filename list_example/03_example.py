# create a list with different type of value and display value and its type
list = [10,20.3,'hello',20]
for i in list:
    if type(i) == int:
        print(f'{i} is int type')
    elif type(i) == float:
        print(f'{i} is float type')
    elif type(i) == str:
        print(f'{i} is string type')