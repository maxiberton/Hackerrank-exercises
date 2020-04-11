def migratoryBirds(arr):
    counter_list = Counter(arr)
    most_common = counter_list.most_common(2)
    if most_common[0][1] == most_common[1][1]:
        if most_common[0][0] < most_common[1][0]:
            return most_common[0][0]
        else:
            return most_common[1][0]
    else:
        return most_common[0][0]