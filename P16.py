#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 21000?

def getsum(num):
    return 0 if num == 0 else (int(num % 10) + getsum(int(num/10)))

print(getsum(2**1000)) 
print(sum([int(char) for char in str(2**1000)]))