def kaprekarNumbers(p, q):
    
    a = [str(i**2) for i in range(p, q+1)]
    
    r = [i[len(i)//2:] for i in a]
    l = [i[:len(i)//2] if i[:len(i)//2] != '' else 0 for i in a]
    
    full = [int(r[i])+int(l[i]) for i in range(len(r))]
    results = [int(a[i])**0.5 for i in range(len(r)) if full[i] == int(a[i])**0.5]
    results1 = [int(i) for i in results]
    
    if any(results):
        print(*results1)
    else:
        print('INVALID RANGE')