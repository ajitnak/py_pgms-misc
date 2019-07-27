def toStr(n):
    digits='0123456789'
    result = ''

    if n==0:
        return '0'
    while n > 0:
        result = digits[n%10] + result
        n = n/10
    return result

print "64560892237 to sitr {}".format(toStr(64560892237))
