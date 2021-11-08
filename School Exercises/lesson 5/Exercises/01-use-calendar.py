import calendar as c

ourCal = c.Calendar()

def allDays(y, m):
    """
    From: https://stackoverflow.com/a/56416995
    """
    return ["{}".format(d) for d in ourCal.itermonthdates(y, m)]

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