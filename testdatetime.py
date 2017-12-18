#coding=utf-8

import datetime

starttime = '2017-01-01'
endtime = '2017-11-30'

starttime = datetime.datetime.strptime(starttime, '%Y-%m-%d')
endtime = datetime.datetime.strptime(endtime, '%Y-%m-%d')

#starttime = datetime.date(2017,1,1)
#endtime = datetime.date(2017,11,30)
delta = (endtime - starttime).days
date1 = starttime + datetime.timedelta(days=2)
print(starttime, endtime, delta)
print(date1)