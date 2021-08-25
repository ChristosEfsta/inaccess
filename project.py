#pip install python-dateutil

import sys
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *



values = sys.stdin.readline()
values_list = values.split()

period = values_list[0]
TIMEzone = values_list[1]
t_1 = values_list[2]
t_2 = values_list[3]


interval_str = period[0:-1] 
interval1 = int(interval_str)

if period[-1]=='d':
#daily period
  dailyinterval = interval1
  dailydates = list(rrule(DAILY, interval=dailyinterval, dtstart=parse(t_1), until=parse(t_2)))

#convert the type of the list
  for j in range (0, len(dailydates)):
   dailydates[j] = dailydates[j].strftime("%Y%m%dT%H%M%SZ")

#print the results
  
  sys.stdout.write('\n'.join(map(str, dailydates))) 


elif period[-1]=='h':
#hourly period
  hourlyinterval = interval1
  hourlydates = list(rrule(HOURLY, interval = hourlyinterval,  dtstart=parse(t_1), until=parse(t_2)))

#convert the type of the list
  for j in range (0, len(hourlydates)):
   hourlydates[j] = hourlydates[j].strftime("%Y%m%dT%H%M%SZ")

#print the results
  
  sys.stdout.write('\n'.join(map(str, hourlydates)))  

elif period[-1]=='m':
#monthly period
  monthlyinterval = interval1
  monthlydates = list(rrule(MONTHLY, interval=monthlyinterval,  dtstart=parse(t_1), until=parse(t_2)))

#convert the type of the list
  for j in range (0, len(monthlydates)):
   monthlydates[j] = monthlydates[j].strftime("%Y%m%dT%H%M%SZ")
  
#print the results
  
  sys.stdout.write('\n'.join(map(str, monthlydates)))  

elif period[-1]=='y':
#yearly period
  yearlyinterval = interval1
  yearlydates = list(rrule(YEARLY, interval=yearlyinterval,  dtstart=parse(t_1), until=parse(t_2)))

#convert the type of the list
  for j in range (0, len(yearlydates)):
   yearlydates[j] = yearlydates[j].strftime("%Y%m%dT%H%M%SZ")
  
#print the results
  
  sys.stdout.write('\n'.join(map(str, yearlydates))) 

else:
 sys.stderr.write("ERROR: Unsupported period")