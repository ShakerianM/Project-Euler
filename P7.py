import math
def Is_Prime(num):
    if num <= 1 :
        return False
    elif num == 2 :
        return True
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: 
            return False
    return True

def ith_Prime(i):
    Prime_count = 2
    num = 3
    while Prime_count < i :
        num += 2
        if Is_Prime(num) :

            Prime_count += 1
    return num

print(ith_Prime(10001))
        


