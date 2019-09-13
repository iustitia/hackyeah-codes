import datetime as dt

monday_weekday = 0
now = dt.date.today()

#############
"""
Wylicz datę pierwszego poniedziałku w przyszłym miesiącu
"""

#############


month = now.month + 1
year = now.year
if month == 13:
    month = 1
    year = year + 1

month_first_day = dt.date(year, month, 1)
diff = 7 - month_first_day.weekday()

first_monday = month_first_day + dt.timedelta(diff)
print(first_monday)
# print(first_monday.weekday())
