import math

def isPrime(n):
    for i in (2, math.sqrt(n) + 1):
        if (n % i == 0):
            return False
    return True

print "is {} boolean: {}".format(17, isPrime(17))
        
