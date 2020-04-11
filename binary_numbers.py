from math import log, modf

def int_part(n):
    int_part = int(modf(log(n, 2))[1])
    return int_part

def binary_numbers(n: int) -> int:
    a = []
    for i in range(int_part(n)):
        a.append(n%2)
        n = n//2
    a.append(1)
    
#No puedo hacer que me tire una de mas si es que hay 3 seguidos ponele
    count = 0
    for i in range(len(a)-1):
        if a[i] == 1 and a[i+1] == 1:
            count += 1
        else:
            count = 1
    
    return count

#De discussion
'''
n = int(input().strip())

numbers = bin(n)[2:].split('0')
lenghts = [len(num) for num in numbers]
print(max(lenghts))
'''