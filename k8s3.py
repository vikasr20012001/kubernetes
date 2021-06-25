#!/usr/bin/python3
print("Content-Type: text/html")
print()


import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
img=cmd.getvalue("a")
cont=cmd.getvalue("b")
rep=cmd.getvalue("s")
st,out=sub.getstatusoutput('sudo kubectl create deployment ' +cont + ' --image='+img+ ' --kubeconfig admin.conf')
if st==0:
    print("Your  Deployment  Successfully Launch : " +out)
else:
    print("Error Occurred \n" + out)
st,res=sub.getstatusoutput('sudo kubectl expose deployment ' +cont + ' --type=NodePort  --port=8080 --kubeconfig admin.conf')
if st==0:
    print("Your service expose  Successfully Launch : " +res)
else:
    print("Error Occurred \n" + res)
st,reps=sub.getstatusoutput('sudo kubectl scale  --replicas=' +rep + " " ' deployment/'  +cont + ' --kubeconfig admin.conf')
if st==0:
    print("Your replica created  Successfully Launch : " +reps)
else:
    print("Error Occurred \n" + reps)
