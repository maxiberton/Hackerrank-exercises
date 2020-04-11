from itertools import permutations

def biggerIsGreater(w):
    abcdario = 'abcdefghijklmnopqrstuvwxyz'
    values = [abcdario.index(c)+1 for c in w]
    permut = [*permutations(values)]
    return min(permut)
    