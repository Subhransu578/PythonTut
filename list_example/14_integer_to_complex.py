list = eval(input('Enter a list: '))
print('**** Original List ****')
print(list)
lint = []
for i in range(len(list)):
    if type(list[i]) == int:
        lint.append(list[i])

for i in range(len(lint)):
    print(complex(lint[i]))