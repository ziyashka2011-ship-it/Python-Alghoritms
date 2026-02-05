import datetime

today = datetime.date.today()
print("Today:", today)

in_7_days = today + datetime.timedelta(days=7)
print("In seven days:", in_7_days)
