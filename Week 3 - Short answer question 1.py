# Short answer question 1
i = int(input('Enter i :'))
j = int(input('Enter j :'))
k = int(input('Enter k :'))

if i < j:
    if j < k:
        i = j
    else:
        j = k

else:
    if j > k:
        j = i
    else:
        i = k
print("i=", i, "j=", j, "k=", k)

# (a) = input : i=3 , j=5 , k=7 | output : i=5 , j=5 , k=7
# (b) = input : i=3 , j=7 , k=5 | output : i=3 , j=5 , k=5
# (c) = input : i=5 , j=3 , k=7 | output : i=7 , j=3 , k=7
# (d) = input : i=5 , j=7 , k=3 | output : i=5 , j=3 , k=3
# (e) = input : i=7 , j=3 , k=5 | output : i=5 , j=3 , k=5
# (f) = input : i=7 , j=5 , k=3 | output : i=7 , j=7 , k=3
