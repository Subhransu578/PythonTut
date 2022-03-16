num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
sum = 0
for i in range(num1, num2+1):
    sum = sum + i
print(f'Sum of {num1} to {num2} is {sum}.')