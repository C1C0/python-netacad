"""
Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time),
 minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.
"""

def formatAsTimeString(hours, minutes, seconds):
    """Format: hh:mm:ss"""
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)


class Timer:
    def __init__( self, hours=0, minutes=0, seconds=0 ):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return formatAsTimeString(self.__hours, self.__minutes, self.__seconds) 

    def next_second(self):
        """adds one second"""
        self.__seconds += 1
        self.__check_all()

    def prev_second(self):
        """goes one second back"""
        self.__seconds -= 1
        self.__check_all()

    def __check_all(self):
        """groups all checks"""
        self.__check_sec()
        self.__check_minute()
        self.__check_hour()

    def __check_sec(self):
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1

        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1

    def __check_minute(self):
        if self.__minutes == 60:
            self.__minutes = 0
            self.__hours += 1

        if self.__minutes < 0:
            self.__minutes = 59
            self.__hours -= 1

    def __check_hour(self):
        if self.__hours == 24:
            self.__hours = 0        

        if self.__hours < 0:
            self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
