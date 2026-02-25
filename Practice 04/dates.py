# Examples of using dates
import datetime
from datetime import timezone, timedelta

now_local = datetime.datetime.now()               # current local date & time
today = datetime.date.today()                     # current date only
current_time = datetime.datetime.now().time()     # current time only

print("Now (local):", now_local)
print("Today:", today)
print("Time:", current_time)
print()

# Creating Date Objects
d = datetime.date(2026, 2, 26)                    # date object: year, month, day
dt = datetime.datetime(2026, 2, 26, 14, 30)       # datetime object: date + time
t = datetime.time(9, 15, 0)                       # time object: hour, minute, second

print("Date:", d)
print("Datetime:", dt)
print("Time:", t)
print()

# Date Formatting (strftime)

dt_now = datetime.datetime.now()                  # current datetime

print("Format YYYY-MM-DD:", dt_now.strftime("%Y-%m-%d"))
print("Format DD/MM/YYYY HH:MM:", dt_now.strftime("%d/%m/%Y %H:%M"))
print("Format Weekday, Month Day:", dt_now.strftime("%A, %B %d"))
print()

# Calculating Time Differences

start = datetime.datetime(2026, 2, 26, 10, 0)     # start moment
end = datetime.datetime(2026, 2, 27, 13, 30)      # end moment

diff = end - start                                # timedelta (difference)

print("Timedelta:", diff)
print("Days:", diff.days)
print("Total seconds:", diff.total_seconds())
print("Hours:", diff.total_seconds() / 3600)
print()

# Working with Timezones

utc_now = datetime.datetime.now(timezone.utc)     # timezone-aware UTC time
print("UTC now:", utc_now)

kz_tz = timezone(timedelta(hours=6))              # timezone offset +06:00
kz_time = utc_now.astimezone(kz_tz)               # convert to +06:00
print("KZ time (+06:00):", kz_time)

local_time = datetime.datetime.now().astimezone() # local time with timezone info
print("Local time:", local_time)



# #%a	Weekday, short version	                        Wed	
# %A	Weekday, full version	                        Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	        3	
# %d	Day of month 01-31	                               31	
# %b	Month name, short version	                    Dec	
# %B	Month name, full version	                    December	
# %m	Month as a number 01-12	                        12	
# %y	Year, short version, without century	        18	
# %Y	Year, full version	                            2018	
# %H	Hour 00-23	                                    17	
# %I	Hour 00-12	                                    05	
# %p	AM/PM	                                        PM	
# %M	Minute 00-59	                                41	
# %S	Second 00-59	                                08	
# %f	Microsecond 000000-999999	                    548513	
# %z	UTC offset	                                    +0100	
# %Z	Timezone	                                    CST	
# %j	Day number of year 001-366	                    365	
# %U	Week number of year, Sunday as the first day of week, 00-53	        52	
# %W	Week number of year, Monday as the first day of week, 00-53	        52	
# %c	Local version of date and time	                Mon Dec 31 17:41:00 2018	
# %C	Century	                                        20	
# %x	Local version of date	                        12/31/18	
# %X	Local version of time	                        17:41:00	
# %%	A % character	                                %	
# %G	ISO 8601 year	                                2018	
# %u	ISO 8601 weekday (1-7)	                        1	
# %V	ISO 8601 weeknumber (01-53)	                    01