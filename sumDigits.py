def sum_digits(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n/10
    return sum

print "sum of digits for {} = {}".format(122326, sum_digits(122326))

    
