# element-wise sum in the tuple:
tup1 = eval(input('Enter 1st tuple: '))
tup2 = eval(input('Enter 2nd tuple: '))
tup3 = eval(input('Enter 3rd tuple: '))
tup = []
print('Tuple is :')
print('Tuple1',tup1)
print('Tuple2',tup2)
print('Tuple3',tup3)
if len(tup1) == len(tup2) == len(tup3):
    length = len(tup1)
    for i in range(length):
        tup.append(tup1[i]+tup2[i]+tup3[i])
else:
    print('Tuple length are not same.')
print(tuple(tup))