def equalizeArray(arr):
    return sum(collections.Counter(arr).values()) - collections.Counter(arr).most_common(1)[0][1]