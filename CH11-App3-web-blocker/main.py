#!/bin/bash/env python3
"""
Program will block access to listed websites within
a scheduled window of time.  Program will run as a
service using very little resources.

@author Ellery J. Penas
@version 2018-04-09
"""
import time
from datetime import datetime as dt


def main():
    # using a dummy host file to test script
    hosts_path = "/projects/python-class-app/hosts"
    redirect_ip = "127.0.0.1"
    website_list = ["facebook.com", "www.facebook.com", "www.youtube.com"]

    while True:
        if dt(
                dt.now().year,
                dt.now().month,
                dt.now().day,
                20) < dt.now() < dt(
                dt.now().year,
                dt.now().month,
                dt.now().day,
                23):
            print("It's work time!!")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect_ip + " " + website + "\n")
        else:
            print("It's fun time!!")
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                file.truncate()

        time.sleep(5)


if __name__ == "__main__":
    main()
