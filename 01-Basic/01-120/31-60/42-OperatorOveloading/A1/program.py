
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

    def __add__(self, other):
        seconds = self.seconds + other.seconds 
        minutes = self.minutes + other.minutes + (seconds // 60 )
        hours = self.hours + other.hours + (minutes // 60)
        NewTime = Time(hours%24, minutes%60, seconds%60)
        return NewTime

WorkTime = Time(10, 15, 28)
PlusProgramming = Time(6, 55, 40)

print(WorkTime + PlusProgramming)

