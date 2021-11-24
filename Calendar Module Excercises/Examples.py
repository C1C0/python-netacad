"""Following doc. provides examples of usage for calendar module"""

from calendar import Calendar as C, TextCalendar as TC, HTMLCalendar as HTMLC
"""
Calendar (C) objects is used for providing data, not formatting
Class don't have static methods to use
"""

import CalendarExamplesFunctions as Ef
"""CalendarExamplesFunctions (Ef) provides helper functions for presenting""" 

ourFirstweekday = 0 
"""Sets first day of week for selected object"""

calendarObj = C(ourFirstweekday)

Ef.iterWeekDays(calendarObj)
Ef.iterMonthDates(calendarObj)
Ef.iterMonthDays(calendarObj)
Ef.iterMonthDays2(calendarObj)
Ef.iterMonthDays3(calendarObj)
Ef.iterMonthDays4(calendarObj)
Ef.monthDatesCalendar(calendarObj)
Ef.monthDays2Calendar(calendarObj)
Ef.yearsDatesCalendar(calendarObj)
Ef.yearsDaysCalendar(calendarObj)
Ef.yearsDays2Calendar(calendarObj)

# Text calendar examples
textCalendarObj = TC(ourFirstweekday)

Ef.formatMonth(textCalendarObj)
Ef.pryear(textCalendarObj)

# HTML calendar examples
htmlCalendarOjb = HTMLC(ourFirstweekday)

Ef.formatMonthHTML(htmlCalendarOjb)
Ef.cssClasses(htmlCalendarOjb)

# Static instances of calendar
Ef.leapDays()