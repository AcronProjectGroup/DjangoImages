import os

class Time:
    def __init__(self, hours, minutes, seconds):
        if hours >= 24 or hours < 0:
            raise ValueError("Hours between 00 to 23")
        if minutes >= 60 or minutes < 0:
            raise ValueError("Minutes between 00 to 59")
        if seconds >= 60 or seconds < 0:
            raise ValueError("Seconds between 00 to 59")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

WorkTime = Time(0, 0, 0)
print(WorkTime)

# os.system('clear')
