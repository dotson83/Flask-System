# Imports
import psutil
import platform
import socket
import os
from flask import Flask, render_template, url_for, send_from_directory
from flask import Markup
import threading

# Operating System
osprint = platform.system()
release = platform.release()

# Operating System Print
os1 = 'OS: ' + osprint
os2 = 'Release: ' + release
os = os1 + '<br>' + os2 + '<br>'

# Hostname
hostname = platform.node()
host = 'Hostname : ' + hostname + '<br>'

# Memory Variables
mem = psutil
virtual = mem.virtual_memory()
total = float(virtual.total) / 1000000
used = float(virtual.used) / 1000000
free = float(virtual.free) / 1000000
available = float(virtual.available) / 1000000
per = float(virtual.percent)
RAM1 = 'Total RAM: ' + str(round(total)) + 'MB<br>'
RAM2 = 'Used RAM: ' + str(round(used)) + 'MB<br>'
RAM3 = 'Free RAM: ' + str(round(free)) + 'MB<br>'
RAM4 = 'Available RAM: ' + str(round(available)) + 'MB<br>'
RAM5 = 'RAM: ' + str(per) + '%<br>'
RAM = RAM1 + RAM2 + RAM3 + RAM4 + RAM5

# CPU Variables
cpu = psutil
percent = cpu.cpu_percent()
count = cpu.cpu_count()
processor1 = 'CPU usage: ' + str(round(percent)) + '%<br>'
processor2 = 'CPU count: ' + str(round(count)) + '%<br>'
processor = processor1 + processor2

# Flask
app = Flask(__name__)

@app.route('/')
def site():
  return render_template('return.html', os=os, host=host, RAM=RAM, processor=processor)

if __name__ == '__main__':
  app.run(port=9111)
