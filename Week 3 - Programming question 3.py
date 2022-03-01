# Programming questions 3
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
d = int(input('Enter d:'))
e = int(input('Enter e:'))

if a == b:
    print('DUPLICATES')
    if a == c:
        print('DUPLICATES')
        if a == d:
            print('DUPLICATES')
            if a == e:
                print('DUPLICATES')
                if b == c:
                    print('DUPLICATES')
                    if b == d:
                        print('DUPLICATES')
                        if b == e:
                            print('DUPLICATES')
                            if c == d:
                                print('DUPLICATES')
                                if c == e:
                                    print('DUPLICATES')
                                    if d == e:
                                        print('DUPLICATES')
else:
    print("ALL UNIQUE")
