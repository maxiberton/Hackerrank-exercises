def jumpingOnClouds(c, k):
    e = 100
    if not len(c)%k:
        for i in range(0, len(c), k):
            if c[i] == 0:
                e -= 1
            else: 
                e -= 3
        
    else:
        d = c * k
        for i in range(0, len(d), k):
            if d[i] == 0:
                e -= 1
            else:
                e -= 3
                
    return e
