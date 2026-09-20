
from datetime import date, timedelta

"""
class DateConverter:
    def __init__(self, date):
        self.date = date
    
    def current_date(self):
        return self.date
    
    def date_to_week(self):
        return self.date / 7
    
    def date_to_month(self):
        return self.date / 30
    
    def date_to_year(self):
        return self.date / 365
    
if __name__ == "__main__":
    date_converter = DateConverter(int(input("Enter the date: ")))
    print(f"Current Date: {date_converter.current_date()}")
    print(f"Weeks: {round(date_converter.date_to_week(), 2)}")
    print(f"Months: {round(date_converter.date_to_month(), 2)}")
    print(f"Years: {round(date_converter.date_to_year(), 2)}")


class DateCalculator:
    def __init__(self, date_obj):
        self.date = date_obj

    def current_date(self):
        return self.date

    def add_days(self, days):
        return self.date + timedelta(days=days)

    def subtract_days(self, days):
        return self.date - timedelta(days=days)

    def add_months(self, months):
        return self.date + timedelta(days=months * 30)

    def subtract_months(self, months):
        return self.date - timedelta(days=months * 30)

    def add_years(self, years):
        return self.date + timedelta(days=years * 365)

    def subtract_years(self, years):
        return self.date - timedelta(days=years * 365)

    def days_between(self, other_date):
        return abs((self.date - other_date).days)

    def months_between(self, other_date):
        return abs((self.date - other_date).days / 30)

    def years_between(self, other_date):
        return abs((self.date - other_date).days / 365)


if __name__ == "__main__":
    date_calculator = DateCalculator(date.today())

    print(f"Current Date: {date_calculator.current_date()}")
    print(f"Add Days: {date_calculator.add_days(10)}")
    print(f"Subtract Days: {date_calculator.subtract_days(10)}")
    print(f"Add Months: {date_calculator.add_months(10)}")
    print(f"Subtract Months: {date_calculator.subtract_months(10)}")
    print(f"Add Years: {date_calculator.add_years(10)}")
    print(f"Subtract Years: {date_calculator.subtract_years(10)}")

    print(f"Days Between: {date_calculator.days_between(date.today())}") 
"""

from datetime import datetime


class YearCalculator:
    def __init__(self, year):
        self.year = year

    def current_year(self):
        return self.year

    def add_years(self, years):
        return self.year + years

    def subtract_years(self, years):
        return self.year - years

    def years_between(self, other_year):
        return abs(self.year - other_year)

    def next_year(self):
        return self.year + 1

    def previous_year(self):
        return self.year - 1

    def days_until_new_year(self):
        now = datetime.now()

        # next year January 1
        next_new_year = datetime(year=now.year + 1, month=1, day=1)
        
        # previous year January 1
        previous_new_year = datetime(year=now.year, month=1, day=1)
        
        # days until next new year
        days_until_next = (next_new_year - now).days
        
        # days until previous new year
        days_until_previous = (now - previous_new_year).days
        
        return days_until_next, days_until_previous
    
if __name__ == "__main__":
    year_calculator = YearCalculator(2025)
    print(f"Current Year: {year_calculator.current_year()}")
    print(f"Add Years: {year_calculator.add_years(10)}")
    print(f"Subtract Years: {year_calculator.subtract_years(10)}")
    print(f"Years Between: {year_calculator.years_between(2020)}")
    print(f"Next Year: {year_calculator.next_year()}")
    print(f"Previous Year: {year_calculator.previous_year()}")
    print(f"Days Until New Year: {year_calculator.days_until_new_year()}")
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






