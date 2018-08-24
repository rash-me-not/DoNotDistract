# importing required libraries time and datetime
import time
from datetime import datetime as dt

# setting the host file path, future version to include auto config to pick Windows v/s linux paths
host_path = r"C:\Windows\System32\drivers\etc\hosts"

# IF Unix- /etc/hosts
#redirect to a motivational website
redirect = "23.253.54.202"

#list of websites which cause distractions to a person (you can add your own list)
website_list = ["www.facebook.com", "facebook.com", "yahoo.com"]
while True:
    if dt(dt.now().year
        ,dt.now().month,
        dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+ website+"\n")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)