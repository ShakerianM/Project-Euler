

def sum(num):
    if num % 3 == 0 or num % 5 == 0 :
        return num
    return 0
sumtotal = 0
for i in range(1000):
    sumtotal += sum(i)

print(sumtotal)