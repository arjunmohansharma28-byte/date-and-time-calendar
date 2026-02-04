import datetime
print("Todays date is", datetime.date.today())
print("Current date and time is",datetime.datetime.now())
from datetime import date , time , datetime
today = date.today()
print("\nDate components", today.year, today.month, today.day)