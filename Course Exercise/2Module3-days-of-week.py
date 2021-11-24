"""
Scenario
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you - this name comes from the fact that objects of 
that class will be able to store and to manipulate days of a week.

The class constructor accepts one argument - a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry,
 we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day 
of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.
"""

class WeekDayError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
	

class Weeker:
    allowed_weekdays: str = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    n_of_weekdays: int = len(allowed_weekdays)
    weekdays_last_index: int = n_of_weekdays - 1

    def __init__(self, day):
        if day not in Weeker.allowed_weekdays:
            raise WeekDayError
        
        self.__actual_day = day

    def __str__(self):
        return self.__actual_day

    def add_days(self, n: int) -> None:
        rest, actual_index = self.__get_indexes(n)
        self.__set_actual_day(rest + actual_index)

    def subtract_days(self, n: int) -> None:
        rest, actual_index = self.__get_indexes(n)
        self.__set_actual_day(actual_index - rest)

    def __get_indexes(self, n : int) -> tuple:
        rest = self.__get_rest(n)
        actual_index = self.__get_actual_day_index()
        return (rest, actual_index)

    def __get_rest(self, n : int) -> int:
        return n % Weeker.n_of_weekdays

    def __get_actual_day_index(self) -> int:
        return Weeker.allowed_weekdays.index(self.__actual_day)

    def __set_actual_day(self, new_index):
        self.__actual_day = Weeker.allowed_weekdays[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
