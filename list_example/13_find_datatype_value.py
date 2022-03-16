list = eval(input('Enter a list: '))
print('**** Original List ****')
print(list)
lint = []
lbool = []
lfloat = []
lcomp = []
lstr = []

for i in range(len(list)):
    if type(list[i]) == int:
        lint.append(list[i])
    elif type(list[i]) == float:
        lfloat.append(list[i])
    elif type(list[i]) == bool:
        lbool.append(list[i])
    elif type(list[i]) == complex:
        lcomp.append(list[i])
    elif type(list[i]) == str:
        lstr.append(list[i])

print('**** Integer List ****')
print(lint)
print()
print('**** Float List ****')
print(lfloat)
print()
print('**** Bool List ****')
print(lbool)
print()
print('**** Complex List ****')
print(lcomp)
print()
print('**** String List ****')
print(lstr)