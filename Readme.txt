I am using windows machine so I didn't creat a shell script

I used Python 2.7 version; Notepad++; windows 10 command prompt to write this code

I used original log.txt file as input without any modifications in size.the following the link:
https://drive.google.com/file/d/0B7-XWjN4ezogbUh6bUl1cV82Tnc/view

Feature F1: List in descending order the top 10 most active hosts/IP addresses that have accessed the site.

code is in process_logf1.py file and src folder
command to run the file: python process_logf1.py
output file: hosts.txt


Feature 2: Identify the top 10 resources on the site that consume the most bandwidth. Bandwidth consumption can be extrapolated from bytes sent over the network and the frequency by which they were accessed.

code is in process_logf2.py file and src folder
command to run the file: python process_logf2.py
output file: resources.txt

Feature F3: List in descending order the site’s 10 busiest (i.e. most frequently visited) 60-minute period.

code is in process_logf3.py file and src folder
command to run the file: python process_logf3.py
output file: hours.txt