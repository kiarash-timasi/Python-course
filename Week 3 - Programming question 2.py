# Programming questions 2
x = int(input('Enter x:'))
y = int(input('Enter y:'))
z = int(input('Enter z:'))

if x*x == y*y + z*z or y*y == x*x + z*z or z*z == x*x + y*y:
    print('Right')
else:
    print('Not Right')
