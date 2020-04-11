def cutTheSticks(arr):
    output = []
    while any(arr):
        toCut = [v for v in arr if v != 0]
        output.append(len(toCut))
        lenght_of_cut = min(toCut)
        arr = [v - lenght_of_cut for v in arr if v >= lenght_of_cut]

    print(output)


cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1])
