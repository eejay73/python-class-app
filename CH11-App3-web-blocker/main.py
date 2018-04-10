#!/bin/bash python3
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
    hosts_path = "./python-class-app/hosts"
    redirect_ip = "127.0.0.1"
    website_list = ["facebook.com", "www.facebook.com", "www.youtube.com"]

    while True:
        if dt(
                dt.now().year,
                dt.now().month,
                dt.now().day,
                8) < dt.now() < dt(
                dt.now().year,
                dt.now().month,
                dt.now().day,
                16):
            print("It's work time!!")
        time.sleep(5)


if __name__ == "__main__":
    main()
