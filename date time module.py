from datetime import datetime
from datetime import date,time
import datetime
# import date
# now = datetime.now()
# print(now)

# today = datetime.today()
# print(today())
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.hour)
# print(today.minute)
# print(today.second)


# print(date.today())

# print(datetime.now())
# print(datetime.today())
# print(date.today())

# #  Creating your own date
# birthday=datetime.date(2008,10-27)
# print(birthday)

# d = datetime.date(2026, 7, 7)

# print(d.year)
# print(d.month)
# print(d.day)
# # in string type

now = datetime.datetime.now()

formatted = now.strftime("%d-%m-%Y")

print(formatted)