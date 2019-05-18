import socket
import commands
import sys
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
result = sock.connect_ex(("127.0.0.1",5000))
if result == 0:
   print "sudi app is reachable"
   sys.exit(0)
else:
   print "i m restarting the app"
   commands.getoutput('sudo -u sudi /webapps/devops/app.py 2>> /var/log/sudiapp.log')
