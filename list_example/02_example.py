# create a list which is not divisible by 10 and 5
list = [10,20,30,27,43]
print(list)
for i in list:
    if i%10!=0 and i%5!=0:
        print(f'{i} is not divisible')