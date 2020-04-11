def sockMerchant(n, ar):
    sock_quant = {i:ar.count(i) for i in ar}
    return sum([i//2 for i in sock_quant.values()])