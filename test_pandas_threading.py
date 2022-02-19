#!/usr/bin/python3
import pandas
import threading

def fetch_file():
    while True:
        url = "https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html"
        pandas.read_html(url)

thread1 = threading.Thread(target = fetch_file)
thread2 = threading.Thread(target = fetch_file)

thread1.start()
thread2.start()

thread1.join()
thread2.join()