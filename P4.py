import math

def Is_Palindrome(num):
    num = str(num)
    if num == num[::-1] :
        return True
    return False

def Palindrome(min_num, max_num):
    Plist = []

    for i in range(min_num, max_num, -1):
        for j in range(min_num, max_num, -1):
            if Is_Palindrome(i * j):
                Plist.append(i * j)
    Plist.sort(reverse=True)
    return Plist[0]




min_num, max_num = 100, 999
#print(Is_Palindrome(max_num))
print(Palindrome(max_num, min_num))
