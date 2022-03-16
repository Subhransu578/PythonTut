# append element from 100 to 200 which is divisible by either 3 or 5:
list = [12,15,23,54,67,81]
print(list)
listApp = []
for i in list:
    if i%3 == 0 or i%5 == 0:
        listApp.append(i)
print(listApp)