# Programming question 1
salary = int(input('Enter Salary :'))
if salary <= 1000:
    taxrate = 0
    tax = salary * 0 / 100
    netincome = salary - tax
    print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 1000:
    if salary <= 2500:
        taxrate = 10
        tax = salary * 10 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 2500:
    if salary <= 4000:
        taxrate = 15
        tax = salary * 15 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 4000:
    if salary <= 6000:
        taxrate = 20
        tax = salary * 20 / 100
        netincome = salary - tax
        print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)
if salary > 8000:
    taxrate = 30
    tax = salary * 30 / 100
    netincome = salary - tax
    print("taxrate=", taxrate, "tax=", tax, "netincome=", netincome)





