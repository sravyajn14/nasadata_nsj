
# Feature F1 : List in descending order the top 10 most active hosts/IP addresses that have accessed the site.
import re
import collections

infile = open("log.txt","r")
ofile=open("hosts.txt","w")
# patterns to match ip address and host names from strings
ip= re.compile(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")
hname= re.compile(r"(\w+)\.(\w+)\.(\w+)")
d={}
total =0
#match ip and hostname from each line and store it in dictionary; find if ip address or hname is in dicitionary; increment the counter if there is same ip address or hname found the dictionary
for line in infile:
    ipm=ip.match(line)
    hnm1=hname.match(line)
    
        
    if ipm:
        key_ip = str(line.split('- -')[0])
        if key_ip in d:
            d[key_ip]  +=1
        else:
            d[key_ip] = 1
        
    elif hnm1:
        key_hname = str(line.split('- -')[0])
        if key_hname in d:
            d[key_hname] +=1
        else:
            d[key_hname] = 1
#sort it in descending order and write it to file
d_view = [ (v,k) for k,v in d.items() ]
d_view.sort(reverse=True) 
n=1
for v,k in d_view:
    ofile.write ("%s, %d \n" % (k,v))
    if n == 10:
        break;
    n += 1

 
