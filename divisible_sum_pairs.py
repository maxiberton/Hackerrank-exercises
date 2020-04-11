def divisibleSumPairs(n, k, ar):
    a = [True for i in range(n) for j in range(i+1,n) if sum([ar[i], ar[j]]) % k == 0]
    print(a.count(True))

divisibleSumPairs(2,2,[8,10])


