#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("dn")
imagename = form.getvalue("i")

output = subprocess.getoutput(f"sudo kubectl create deployment {depname} --image={imagename}")
time.sleep(2)
print(output)

