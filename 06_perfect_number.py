num = int(input('Enter a number: '))
sum = 0
for i in range(1, num):
    rem = num % i
    if rem == 0:
        sum = sum + i
if sum == num:
    print('perfect')
else:
    print('not perfect')