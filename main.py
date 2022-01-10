import requests
import csv
import threading

filename = "salvia_rosmarinus.csv"


def open_file(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data.pop(0)
        return data
    

def do_request(data):
    counter = 1

    for row in data:
        url = row[0]
        url = url.replace("medium","large")
        r = requests.get(url, allow_redirects=True)
        open('image'+str(counter)+'.jpg', 'wb').write(r.content)
        print(counter)
        counter = counter+1

data = open_file(filename)
do_request(data)
