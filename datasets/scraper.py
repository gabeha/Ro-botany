import requests
import csv

filename = "thymus_vulgaris.csv"


def open_file(filename):
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))
        data.pop(0)
        data_new=[]
        for x in data:
            if x:
                data_new.append(x)

        return data_new


def do_request(data):
    counter = 1

    for row in data:
        try:
            url = row[0]
        #url = url.replace("medium","large")
            r = requests.get(url, allow_redirects=True)
            open('image'+str(counter)+'.jpg', 'wb').write(r.content)

        except:
            pass

        print(counter)
        counter = counter+1

data = open_file(filename)
do_request(data)
