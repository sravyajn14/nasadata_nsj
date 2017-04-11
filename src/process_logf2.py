# Feature F2: Identify the top 10 resources on the site that consume the most bandwidth. Bandwidth consumption can be extrapolated from bytes sent over the network and the frequency by which they were accessed.
import re
import string
import operator
#read input file
infile = open("log.txt","r")
#write to output file
ofile=open("resources.txt","w")
d={}
for line in infile:
	split_line_spaces= line.split()
	speed = split_line_spaces[len(split_line_spaces)-1]
	key_res = str(line.split()[6])
	#try catch block to skip unwanted characters like '-'
	try:
		if key_res in d:
			d[key_res] = int(speed) + d[key_res]
		else:
			d[key_res] = int(speed)
	except ValueError:
		continue

#sorting the dictionary in descending order		
d_view = [ (v,k) for k,v in d.items() ]
d_view.sort(reverse=True) 
n=1
#writng the dictionary to file
for v,k in d_view:
    ofile.write ("%s, %d\n" % (k,v))
    if n == 10:
        break;
    n += 1
#closing the input and output file	
infile.close()		
ofile.close()
