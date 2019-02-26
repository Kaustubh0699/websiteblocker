import time
from datetime import datetime as dt

host_copy = "hosts"
hosts_path = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]



while True:
    if((dt(dt.now().year,dt.now().month,dt.now().day,0)) < dt.now() < (dt(dt.now().year,dt.now().month,dt.now().day,3))):
        file = open(hosts_path,"r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect+" "+website + "\n")
    else:
        print("hello")
    time.sleep(5)

