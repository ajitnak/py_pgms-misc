def findDivisors(n1, n2):
    divisors = ()
    minVal, maxVal = None, None
    for i in range(2, min(n1,n2) + 1 ):
        if n1%i == 0 and n2%i == 0:
            if  minVal == None or i  < minVal:
                minVal = i
            if  maxVal == None or i  > maxVal:
                maxVal = i
    return minVal, maxVal

divisors = findDivisors(36, 90)
print divisors


