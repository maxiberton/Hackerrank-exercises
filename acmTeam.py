from itertools import combinations
def acmTeam(topic):
    x=[sum(a=='1' or b=='1' for a,b in zip(a,b)) for a,b in combinations(topic,2)]
    m=max(x)
    return m,sum(m==x for x in x)


topic = ['10010', '10110', '11001', '11110', '10100']

e = acmTeam(topic)

