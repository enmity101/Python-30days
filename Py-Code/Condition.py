# if condition
x = 5
y = 3
if x > y:
    print('Hello')

# check if you are eligible to vote or not

age = input('Enter your age: ')
if int(age)>= 18 and int(age) <= 120:
    print('Eligible to vote: ')
else :
    print('Not eligible to vote: ')

# Greatest among three variables
x = 3
y = 4
z = 6
if x > y and x > z:
    print("x is greatest")
elif y > x and y > z:
    print("y is greatest")
else:
    print("z is greatest")

# last digit of the number is divisible by 2 or not
x = int(input('Enter a number: '))
if x % 10 % 2 == 0:
    print('Last digit is divisible by 2')
else:    print('Last digit is not divisible by 2')

