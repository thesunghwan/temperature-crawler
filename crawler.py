import json
import urllib.request

response = urllib.request.urlopen("http://api.wunderground.com/api/65f29d617d92d50b/hourly/q/KR/Pohang.json")

data = json.loads(response.read().decode('utf-8'))
twelve_hours_later = data["hourly_forecast"][12]

pretty = twelve_hours_later["FCTTIME"]["pretty"]
year = twelve_hours_later["FCTTIME"]["year"]
month = twelve_hours_later["FCTTIME"]["mon"]
day = twelve_hours_later["FCTTIME"]["mday"]
date = year + "/" + month + "/" + day

hour = twelve_hours_later["FCTTIME"]["hour"]

temp = twelve_hours_later["temp"]

dictionary = {
    "date": date,
    "hour": hour,
    "datetime": pretty,
    "F": temp["english"],
    "C": temp["metric"]
}

array = [
    date, hour, temp["english"], temp["metric"]
]

read_file = []
with open("sample.csv", "r") as thefile:
    first_line = thefile.readline()
    if(first_line):
        if(first_line.split(",")[0] != "date"):
            read_file.append("date,hour,F,C\n")
            read_file.append(first_line)
        else:
            read_file.append(first_line)
    else:
        read_file.append("date,hour,F,C\n")

    for line in thefile:
        read_file.append(line)

    thefile.close()

if(read_file[-1].split(",")[0] != array[0] or read_file[-1].split(",")[1] != array[1]):
    with open("sample.csv", "w") as thefile:
        for line in read_file:
            thefile.write(line)
        thefile.write(",".join(array) + "\n")
        thefile.close()
