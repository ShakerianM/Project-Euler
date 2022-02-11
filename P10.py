

from P7 import Is_Prime

sum = 2
for i in range(3,2000000,2):
    if Is_Prime(i):
        sum += i


print(sum)
