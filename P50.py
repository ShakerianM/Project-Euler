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

PrimeList = []
PrimeConSum = {}

for i in range(999999, 999, -1):
    if Is_Prime(i):
        PrimeList.append(i)

print(PrimeList.__len__())
for i in range(len(PrimeList), 999, -1):
    for j in range(len(PrimeList)- i, ):

        sumConP = sum(PrimeList[i:i+j])
        if Is_Prime(sumConP) and sumConP < 999999:
            PrimeConSum[str((i,j))] = sumConP



#print(ith_Prime(10001))
        


