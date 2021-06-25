#!/usr/bin/python3
print("Content-Type: text/html")    
print()          
                   

import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
img=cmd.getvalue("x")
cont=cmd.getvalue("y")
st,out=sub.getstatusoutput('sudo kubectl run ' +cont + ' --image='+img+ ' --kubeconfig admin.conf')
if st==0:
    print("Your POD  Successfully Launch : " +out)
else:
    print("Error Occurred \n" + out)
