import math
def Prime(num):
    while num % 2 == 0:
            maxP = 2
            num /= 2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            maxP = i
            num /= i
    if num > 2 :
        maxP = num
    return maxP


num = 600851475143
print(Prime(num))
