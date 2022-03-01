# Short answer question 2
val = int(input())
if val < 10:
    if val != 5:
        print("WoW", end='')
    else:
        val += 1
else:
    if val == 17:
        val += 10
    else:
        print("Whoa", end='')
print(val)

# (a)= input: 3 | output: WoW3
# (b)= input: 21 | output: Whoa21
# (c)= input: 5 | output: 6
# (d)= input: 17 | output: 27
# (d)= input: -5 | output: WoW-5
