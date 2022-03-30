numbers_array = []
for n in range(20):
    number = float(input("Please enter the numbers"))
    numbers_array.append(number)

print("numbers: ", numbers_array)
print("minimum: ", (min(numbers_array)))
print("maximum: ", (max(numbers_array)))
print("result of Sum: ", sum(numbers_array))
print("average: ", sum(numbers_array)/len(numbers_array))
