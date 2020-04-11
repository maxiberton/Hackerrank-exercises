def countingValleys(n, s):
    
    valleys = 0
    alt = 0

    for i in s:
        if i == 'U':
            alt += 1
        else:
            alt -= 1
        if alt == 0 and i == 'U':
            valleys += 1
    return valleys

s = 'UDDUDU'
n = 6

countingValleys(n,s)
