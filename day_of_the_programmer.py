def dayOfProgrammer(year):
    if year > 1918:    
        if year % 400 == 0:
            day = 12
        elif year % 4 == 0 and year % 100 != 0:
            day = 12
        else:
            day = 13
    elif year == 1918:
        day = 26    
    else:
        if year % 4 == 0:
            day = 12
        else:
            day = 13
    
    date1 = datetime.date(year, 9, day).strftime('%d.%m.%Y')
    return date1