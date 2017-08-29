#! python3
import datetime, time
print(datetime.datetime.now())
dt = datetime.datetime(2015,10,21,16,29,0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute,dt.second)

#print(datetime.datetime.fromtimestamp())
print(datetime.datetime.fromtimestamp(100000))
print(datetime.datetime.fromtimestamp(time.time()))

halloween2015 = datetime.datetime(2015,10,31,0,0,0)
newyear2016 = datetime.datetime(2016,1,1,0,0,0)
oct31_2015 = datetime.datetime(2015,10,31,0,0,0)
print(halloween2015 == oct31_2015)
print(halloween2015 > newyear2016)
print(newyear2016 > halloween2015)
print(newyear2016 != oct31_2015)

detal = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(detal.days, detal.seconds, detal.microseconds)
print(detal.total_seconds())
print(str(detal))

dtn = datetime.datetime.now()
print(dtn)
thousandDays = datetime.timedelta(days=1000)
print(dtn + thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365*30)
print(oct21st)
print(oct21st-aboutThirtyYears)
print(oct21st-2*aboutThirtyYears)


print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

#print(datetime.datetime.strftime('October of 15','%B of %y')
