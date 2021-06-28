#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
podname = form.getvalue("p")
imagename = form.getvalue("i")

output = subprocess.getoutput(f"sudo kubectl run {podname} --image={imagename}")
time.sleep(2)
print(output)

