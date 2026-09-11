
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
