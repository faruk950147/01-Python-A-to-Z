"""
class SecondConverter:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def second_to_minute(self):
        return self.seconds / 60
    
    def second_to_hour(self):
        return self.seconds / 3600
    
    def second_to_day(self):
        return self.seconds / 86400
       
if __name__ == "__main__":
    time_converter = SecondConverter(int(input("Enter the seconds: ")))
    print(f"Minutes: {time_converter.second_to_minute()}")
    print(f"Hours: {time_converter.second_to_hour()}")
    print(f"Days: {time_converter.second_to_day()}")


class MinuteConverter:
    def __init__(self, minutes):
        self.minutes = minutes
        
    def minute_to_second(self):
        return self.minutes * 60
    
    def minute_to_hour(self):
        return self.minutes / 60
    
    def minute_to_day(self):
        return self.minutes / 1440
       
if __name__ == "__main__":
    minute_converter = MinuteConverter(int(input("Enter the minutes: ")))
    print(f"Seconds: {minute_converter.minute_to_second()}")
    print(f"Hours: {minute_converter.minute_to_hour()}")
    print(f"Days: {minute_converter.minute_to_day()}")


class HourConverter:
    def __init__(self, hours):
        self.hours = hours
        
    def hour_to_second(self):
        return self.hours * 3600
    
    def hour_to_minute(self):
        return self.hours * 60
    
    def hour_to_day(self):
        return self.hours / 24
       
if __name__ == "__main__":
    hour_converter = HourConverter(int(input("Enter the hours: ")))
    print(f"Seconds: {hour_converter.hour_to_second()}")
    print(f"Minutes: {hour_converter.hour_to_minute()}")
    print(f"Days: {hour_converter.hour_to_day()}")

class DayConverter:
    def __init__(self, days):
        self.days = days
        
    def day_to_second(self):
        return self.days * 86400
    
    def day_to_minute(self):
        return self.days * 1440
    
    def day_to_hour(self):
        return self.days * 24
       
if __name__ == "__main__":
    day_converter = DayConverter(int(input("Enter the days: ")))
    print(f"Seconds: {day_converter.day_to_second()}")
    print(f"Minutes: {day_converter.day_to_minute()}")
    print(f"Hours: {day_converter.day_to_hour()}")

"""
class DateConverter:
    def __init__(self, date):
        self.date = date
    
    def date_to_second(self):
        return self.date * 86400
    
    def date_to_minute(self):
        return self.date * 1440
    
    def date_to_hour(self):
        return self.date * 24
    
if __name__ == "__main__":
    date_converter = DateConverter(int(input("Enter the date: ")))
    print(f"Seconds: {date_converter.date_to_second()}")
    print(f"Minutes: {date_converter.date_to_minute()}")
    print(f"Hours: {date_converter.date_to_hour()}")






