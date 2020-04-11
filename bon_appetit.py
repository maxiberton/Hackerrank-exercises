def bonAppetit(bill, k, b):
    a = (sum([i for i in bill]) - bill[k])/2
    if b == a:
        print('Bon Appetit')
    else:
        print(int(bill[k]/2))