import datetime
from tkinter import Y


my_data = datetime.datetime(2021, 6, 25)

time_now = datetime.datetime.now()

diff_Day = time_now - my_data

x = my_data.strftime("%Y-%m-%d")
y = time_now.strftime("%Y-%m-%d")

print(time_now.strftime("%Y - %m -%d"))


print(f"Days from {x} To {y} => {diff_Day.days}")

# .strftime("%Y - %m -%d")

print("*" * 40)

# ====================task 2 ==========================================

date_now = datetime.datetime.now()

print(date_now.strftime("%Y-%m-%d"))

print(date_now.strftime("%b %m, %Y"))

print(date_now.strftime("%d - %b - %Y"))

print(date_now.strftime("%d / %b / %y"))

print(date_now.strftime("%d / %B / %Y"))

print(date_now.strftime("%a, %d  %b  %Y"))
