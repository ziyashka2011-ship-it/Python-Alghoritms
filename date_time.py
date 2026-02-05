import datetime

today = datetime.date.today()
print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time and date is:", now)

tomorrow = datetime.date(2025,10,8)
print("Tommorow's date is:", tomorrow)


print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
print("Formatted date is:", formatted_date)
formatted_time = now.strftime("%H:%M:%S")
print("Formatted time is:", formatted_time)
weekday = now.strftime("%A")
print("Today is:", weekday)

difference = datetime.date.today() - datetime.date(2011,12,29)
print("Days since 29th December 2011:", difference.days)