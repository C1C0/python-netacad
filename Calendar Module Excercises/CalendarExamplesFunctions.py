from datetime import datetime as DT
from calendar import Calendar, HTMLCalendar, TextCalendar, leapdays
"""Examples based on: https://docs.python.org/3/library/calendar.html"""

def iterWeekDays(c: Calendar) -> None:
    """Example for Calendar calendar.iterweekdays"""
    __myPrint("calendar.iterweekdays")
    print(list(c.iterweekdays()))

def iterMonthDates(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example for Calendar calendar.itermonthdates"""
    __myPrint("calendar.itermonthdates")
    print(list(c.itermonthdates(year, month)))

def iterMonthDays(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.itermonthdays"""
    """0 - days before and after the month finishing the week"""
    __myPrint("calendar.itermonthdays")
    print(list(c.itermonthdays(year, month)))

def iterMonthDays2(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.itermonthdays2"""
    __myPrint("calendar.itermonthdays2")
    print(list(c.itermonthdays2(year, month)))

def iterMonthDays3(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.itermonthdays3"""
    __myPrint("calendar.itermonthdays3")
    print(list(c.itermonthdays3(year, month)))

def iterMonthDays4(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.itermonthdays4"""
    __myPrint("calendar.itermonthdays4")
    print(list(c.itermonthdays4(year, month)))

def monthDatesCalendar(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.monthdatescalendar"""
    __myPrint("calendar.monthdatescalendar")
    print(list(c.monthdatescalendar(year, month)))

def monthDaysCalendar(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.monthdayscalendar"""
    __myPrint("calendar.monthdayscalendar")
    print(list(c.monthdayscalendar(year, month)))

def monthDays2Calendar(c: Calendar, year = DT.now().year, month = DT.now().month) -> None:
    """Example of Calendar calendar.monthdays2calendar"""
    __myPrint("calendar.monthdays2calendar")
    print(list(c.monthdays2calendar(year, month)))

def yearsDatesCalendar(c: Calendar, width = 3, year = DT.now().year) -> None:
    """Example of Calendar calendar.yeardatescalendar"""
    __myPrint("calendar.yeardatescalendar")
    print(list(c.yeardatescalendar(year, width)))

def yearsDays2Calendar(c: Calendar, width = 3, year = DT.now().year) -> None:
    """Example of Calendar calendar.yeardays2calendar"""
    __myPrint("calendar.yeardays2calendar")
    print(list(c.yeardays2calendar(year, width)))

def yearsDaysCalendar(c: Calendar, width = 3, year = DT.now().year) -> None:
    """Example of Calendar calendar.yeardayscalendar"""
    __myPrint("calendar.yeardayscalendar")
    print(list(c.yeardays2calendar(year, width)))

def formatMonth(tc: TextCalendar, theyear = DT.now().year, themonth = DT.now().month, w=1, l=0) -> None:
    """Example of TextCalendar TextCalendar.formatmonth"""
    __myPrint("TextCalendar.formatmonth")
    print(tc.formatmonth(theyear, themonth, w, l))

def pryear(tc: TextCalendar, theyear = DT.now().year, w=2, l=1, c=6, m=3) -> None:
    """Example of TextCalendar TextCalendar.pryear"""
    __myPrint("TextCalendar.pryear")
    tc.pryear(theyear, w, l, c, m)

def formatMonthHTML(htmlC: HTMLCalendar, theyear = DT.now().year, themonth = DT.now().month, withyear=False) -> None:
    """Example of HTMLCalendar HTMLCalendar.formatmonth"""
    __myPrint("HTMLCalendar.formatmonth")
    print(htmlC.formatmonth(theyear, themonth, withyear))

def cssClasses(htmlC: HTMLCalendar) -> None:
    """Example of HTMLCalendar HTMLCalendar.formatmonth"""
    __myPrint("HTMLCalendar.formatmonth")
    print(htmlC.cssclasses)

def leapDays(y1=2000, y2=DT.now().year):
    """Example of Calendar Calendar.leapdays"""
    __myPrint("Calendar.leapdays")
    print(leapdays(y1, y2))

# Private

def __myPrint(message = '') -> None:
    """Modified print output"""
    print("\n\n"+message, end="\n")