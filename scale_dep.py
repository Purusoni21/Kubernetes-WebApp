#!/usr/bin/python3

print("Context-Type:text/plain")
print()

import cgi 
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("a")
rep = form.getvalue("b")
output = subprocess.getoutput(f"sudo kubectl scale deployment {depname}                 --replicas={rep}")
time.sleep(2)
print(output)
