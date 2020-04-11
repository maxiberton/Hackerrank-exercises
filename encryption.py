def encryption(s):
    c = ceil(sqrt(len(s)))
    return ' '.join(map(lambda x: s[x::c], range(c)))