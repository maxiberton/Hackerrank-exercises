def repeatedString(s, n):
    num = n//len(s) 
    slice_of_s = s[:n%len(s)]
    count = s.count('a') * num + slice_of_s.count('a')
    return count
