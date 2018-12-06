import datetime

date = datetime.date(1901, 1, 6)

count = 0
while date < datetime.date(2001, 1, 1):
    if date.day == 1:
        count +=1
    date += datetime.timedelta(days=7)

print count