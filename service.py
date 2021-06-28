#!/usr/bin/python3

print("Content-Type:text/plain")
print()

import cgi
import subprocess
import time

form = cgi.FieldStorage()
depname = form.getvalue("d")
port = form.getvalue("p") 
Type = form.getvalue("t")

output = subprocess.getoutput(f"sudo kubectl expose deployment {depname} --port={port} --type={Type}")
time.sleep(2)
print(output)
