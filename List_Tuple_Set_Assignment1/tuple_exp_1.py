# remove empty tuple
tup = [(),(),("",),('a','b'),('a','b','c'),('d')]
print('Before remove')
print(tup)
t1 = []
for i in tup:
    if i != ():
        t1.append(i)
print('After remove')
print(t1)