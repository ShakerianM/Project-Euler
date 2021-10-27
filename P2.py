
a1 = 1
an = 2
sumEven = 0
while an <= 4000000 :
    if an % 2 == 0 :
        sumEven += an
    swap = an
    an += a1
    a1 = swap
print(sumEven)
