import datetime

# constructs date object!
dt = datetime.date(2029, 11, 4)
print(dt)

# get tpdays date
tdy = datetime.date.today()
print(tdy, tdy.day)

# Monday - 0, Sunday - 6
print(tdy.weekday())

# Monday - 1, Sunday - 7
print(tdy.isoweekday())

# Time deltas
# Date obj = Date obj (+/-) t_delta obj
t_del = datetime.timedelta(days=7)
dtw = tdy + t_del
print(tdy, dtw)

dtw = tdy - t_del
print(tdy, dtw)


# T delta obj = Date obj (+/-) Date obj
bday = datetime.date(2029, 11, 29)
till_bday = bday - tdy
print(till_bday, till_bday.days, till_bday.seconds)

# date times
d1 = datetime.datetime(2024, 11, 23, 12, 30, 34, 1000)
print(d1, d1.date(), d1.time(), d1.year, d1.hour, d1.microsecond)

d2 = datetime.datetime.now()
print(d2)

# timeone aware datetimes
import pytz

d2_utc = datetime.datetime.now(tz=pytz.UTC)
print(d2_utc)

d2 = d2_utc.astimezone(pytz.timezone("Asia/Kolkata"))
print(d2)

for tz in pytz.all_timezones:
    print(tz)

# time to string format
print(d2.strftime("%B %d, %Y"))

# String to date time
d2_str = "July 26, 2024"
dt = datetime.datetime.strptime(d2_str, "%B %d, %Y")
print(dt)
