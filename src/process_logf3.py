import re
import string
import operator
import time
from datetime import timedelta,date,time,datetime
#read the input file
infile = open("log.txt","r")
#open the output file 
ofile=open("hours.txt","w")
#intialize values
prev=0
curr=0
year=1995
month= 7
dict_hrs={}
flag= 0
count =0
s= '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 0'
i=0
for line in infile:
	#the time will reset whenever it increments to next date or minute or hour
	if flag==0:
		currs= line[line.find("[")+1:line.find("]")]
		prevs = currs
	else:
		currs=line[line.find("[")+1:line.find("]")]
	#spilting the date,day,hours,miutes and seconds from the input line of file
	date1 =str(currs.split(':')[0])
	day=int(date1.split('/')[0])
	hrs = int(s.split(':')[1])
	mins= int(s.split(':')[2])
	secs= int((s.split(':')[3]).split('-0400')[0])
	t= time(hrs,mins,secs)
	d= date(year,month,day)
	#current date and time
	cdt= datetime.combine(d,t)
	#first iteration of file
	if i==0:
		pdt=cdt
		i=1
	# gives difference between current date & time and present date & time	
	timedelta= cdt-pdt	
	#abs() functions gives the difference between two dates.the counter increments until it changes to next date
	if abs(timedelta.total_seconds()/60)<1:
		count= count+1
		flag=1
	#storing the values in dictionary of first date and its count;resetting other values
	else:
		dict_hrs[prevs] = count
		count= 0
		flag= 0
		pdt= cdt
#sorting it in descending order and storing it into file	
d_view = [ (v,k) for k,v in dict_hrs.items() ]
d_view.sort(reverse=True) 
n=1
for v,k in d_view:
	ofile.write ("%s, %d\n" % (k,v))
	if n == 10:
		break;
	n += 1
infile.close()		
ofile.close()