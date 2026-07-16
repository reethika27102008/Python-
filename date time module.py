# from datetime import datetime
# from datetime import date,time,timedelta

# from datetime import datetime
# Python uses 12:00 AM (midnight)
# Divides seconds by 3600
# 1 hour = 3600 seconds

# def counter():
#     day = int(input("Enter your day: "))
#     month = int(input("Enter your month: "))
#     year = int(input("Enter your year: "))

#     hour = int(input("Enter hour (1-12): "))
#     minute = int(input("Enter minute: "))
#     am_pm = input("Enter AM or PM: ")

#     if am_pm.upper() == "PM" and hour != 12:
#         hour += 12
#     elif am_pm.upper() == "AM" and hour == 12:
#         hour = 0

#     event_date = datetime(year, month, day, hour, minute)
#     today = datetime.today()

#     difference = event_date - today

#     totaldays = difference.days
#     totalhrs = difference.seconds // 3600
#     totalmin = (difference.seconds % 3600) // 60

#     print("Event date:", event_date.strftime("%Y-%m-%d %I:%M %p"))
#     print(totaldays, "days")
#     print(totalhrs, "hours")
#     print(totalmin, "minutes")

# counter()
# # import datetime
# # import date

# # now = datetime.now()
# # print(now)

# # day=date.today()
# # print(day)

# # t=time.now()
# # print(t)

# today = datetime.today()
# # print(today())
# print(today.year)
# # print(today.month)
# # print(today.day)
# # print(today.hour)
# # print(today.minute)
# # print(today.second)

# # print(datetime.now())

# # now = datetime.now()

# # string format
# # print(now.strftime("%d-%m-%Y"))
# # print(now.strftime("%I:%M %p"))

# # print(now.strftime("%d|%m|%y"))
# # print(now.strftime("%I:%S %p"))

# # #  Creating your own date
# # birthday=datetime.date(2008,10-27)
# # print(birthday)

# # d = datetime.date(2026, 7, 7)

# # print(d.year)
# # print(d.month)
# # print(d.day)


# # # timedelta
# # d1 = date(2026, 7, 8)
# # d2 = date(2026, 10, 27 )

# # difference = d1 - d2
# # print(abs(difference))

# # to add days

# # today = date.today()
# future = date.today() + timedelta(days=26)
# print(future)

# # age calculator
# def birthday():
#     a=int(input("Enter your birth date:"))
#     b=int(input("Enter your birth month:"))
#     c=int(input("Enter your birth year:"))
#     today = datetime.today()
#     difference=today.year-c
#     print(difference)
# birthday()

# # days alived calculator
# def totaldays():
#     day = int(input("Enter birth day: "))
#     month = int(input("Enter birth month: "))
#     year = int(input("Enter birth year: "))
#     birth_date = datetime(year, month, day)
#     today = datetime.today()
#     days_alive = (today - birth_date).days
#     print(days_alive)
# totaldays()

# Countdown
# def counter():
#     day = int(input("Enter your day: "))
#     month = int(input("Enter your month: "))
#     year = int(input("Enter your year: "))

#     event_date = datetime(year, month, day)
#     today = datetime.today()

#     totaldays = (event_date - today).days
#     totalhrs = (event_date - today).seconds // 3600
#     totalmin = ((event_date - today).seconds % 3600) // 60

#     print(totaldays, "days")
#     print(totalhrs, "hours")
#     print(totalmin, "minutes")

# counter()

# # birthday countdown


# def totaldays():
#     day = int(input("Enter birth day: "))
#     month = int(input("Enter birth month: "))
#     year = int(input("Enter birth year: "))
#     birth_date = datetime(year, month, day)
#     today = datetime.today()
#     next_birthday = datetime(today.year, month, day)
#     days_remaining = (next_birthday - today).days
#     print("Your next birthday is in", days_remaining, "days")

# # totaldays()

# worked time
# from datetime import datetime

# def worked_time():
#     start_time = input("Enter start time : ")
#     end_time = input("Enter end time : ")

#     start = datetime.strptime(start_time, "%H:%M")
#     end = datetime.strptime(end_time, "%H:%M")

#     difference = end - start

#     hours = difference.seconds // 3600
#     minutes = (difference.seconds % 3600) // 60

#     print("Total working hours:", hours, "hours", minutes, "minutes")

# worked_time()