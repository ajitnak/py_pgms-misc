def findDivisiors(n1, n2):
    divisiors = ()
    for i in range (1, min(n1, n2)+1):
        if (n1%i == 0) and (n2%i == 0):
            divisiors = divisiors + (i,)
    print "type: {}".format(type(divisiors))
    return divisiors

print "Divisorss for 10, 20: {}".format(findDivisiors(50, 100))
