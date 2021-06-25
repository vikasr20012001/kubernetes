#!/usr/bin/python3
print("Content-Type: text/html")
print()

import time
import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
doc=cmd.getvalue("z")
out=sub.getstatusoutput('sudo '+doc)
if out[0]==0:
    print(out[1])
    time.sleep(5)
    
else:
    print("Please Enter Valid Command")
