x = 1
y = 10000
print("Armstrong Numbers are: ")
for Number in range(x, y):
    digits = 0
    temp = Number
    while temp > 0:  # no of digits
        digits = digits + 1
        temp = temp // 10
    sum = 0
    temp = Number
    while temp > 0:  # calculate armstrong number
        last_digit = temp % 10
        sum = sum + (last_digit ** digits)
        temp = temp // 10
    if Number == sum:
        print(Number)
