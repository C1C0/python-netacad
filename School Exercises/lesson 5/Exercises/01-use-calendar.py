import calendar as c

def allDays(y, m):
    """
    From: https://stackoverflow.com/a/56416995
    """
    return ['{:04d}-{:02d}-{:02d}'.format(y, m, d) for d in range(1, c.monthrange(y, m)[1] + 1)]

def stringAllDates(y, m):
    dates = ""
    for day in allDays(y, m):
        dates += day + "\n"
    
    return dates

print(c.month(2015, 12))
print(c.month(1999, 9))

print("Printing dates\n\n")
print("December 2015\n", stringAllDates(2015, 12), sep="")
print("September 1999\n", stringAllDates(1999, 9), sep="")