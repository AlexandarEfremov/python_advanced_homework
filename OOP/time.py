from datetime import datetime, time, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        current_time = datetime(1, 1, 1, self.hours, self.minutes, self.seconds).strftime("%H:%M:%S")
        return current_time

    def next_second(self):
        if Time.max_seconds >= self.seconds + 1:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes + 1 <= Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours + 1 <= Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0
        current_time = datetime(1, 1, 1, self.hours, self.minutes, self.seconds).strftime("%H:%M:%S")
        return current_time


time = Time(23, 59, 59)

print(time.next_second())
