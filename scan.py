import subprocess
import re
import csv
import datetime

name = "(?:report for )(\S+)"
ip = "(?:\()(\d+.*)(?:\))(?!\.|[ scanned])" 
mac = "(?:MAC Address: )(.+)"

result = subprocess.check_output(['nmap','-sPPn', '192.168.1.1-255'])

with open("logs.csv", 'a') as logs:
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    fieldnames = ["time", "name", "ip", "mac"]
    writer = csv.DictWriter(logs, fieldnames=fieldnames)
    
    names = re.findall(name, result)
    ips = re.findall(ip, result)
    macs = re.findall(mac, result)

    for idx in range(0, len(names) - 1):
        print "Got {}".format(names[idx])
        writer.writerow({"time": time, "name": names[idx], "ip": ips[idx], "mac": macs[idx]})





