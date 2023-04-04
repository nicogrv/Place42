import requests
import time
import datetime
import os



now = datetime.datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
nowsort = ''
debug = open("DEBUG_PATH", 'a')
debug.write(str(date_time_str)+"\t")

if (now.hour == 5 and now.minute <= 15):
    file = open('DEBUG_PATH', 'w+')
    file.write("0000")
    quit(0)

data = {
    'grant_type': 'client_credentials',
    'client_id': 'TOKEN',
    'client_secret': 'TOKEN',
}

r = requests.post('https://api.intra.42.fr/oauth/token', data=data)
str = r.text
i = 0
while (str[i] != ':'):
    i = i + 1
i = i + 2
token = ""
while (str[i] != '"'):
    token = token + str[i]
    i = i + 1
time.sleep(2)

headers = {
    'Authorization': 'Bearer ' + token,
}
r = requests.get('https://api.intra.42.fr/v2/users/USER1', headers=headers)
info = r.text
user1 = ""
i = 0
j = 0
i = info.find("location") + 10
if (info[i] == '"'):
    i = i + 1
while (info[i + j] != '"' and info[i + j] != ','):
    user1 = user1 + info[i + j]
    j = j + 1
debug.write(user1 + "\t")
print("user1 = "+ user1)
time.sleep(2)

r = requests.get('https://api.intra.42.fr/v2/users/USER2', headers=headers)
info = r.text
user2 = ""
i = 0
j = 0
i = info.find("location") + 10
if (info[i] == '"'):
    i = i + 1
while (info[i + j] != '"' and info[i + j] != ','):
    user2 = user2 + info[i + j]
    j = j + 1
debug.write(user2 + "\t")
print("user2 = "+ user2)
time.sleep(2)

r = requests.get('https://api.intra.42.fr/v2/users/USER3', headers=headers)
info = r.text
user3 = ""
i = 0
j = 0
i = info.find("location") + 10
if (info[i] == '"'):
    i = i + 1
while (info[i + j] != '"' and info[i + j] != ','):
    user3 = user3 + info[i + j]
    j = j + 1
debug.write(user3 + "\t")
print("user3 = "+ user3)
time.sleep(2)

r = requests.get('https://api.intra.42.fr/v2/users/USER4', headers=headers)
info = r.text
user4 = ""
i = 0
j = 0
i = info.find("location") + 10
if (info[i] == '"'):
    i = i + 1
while (info[i + j] != '"' and info[i + j] != ','):
    user4 = user4 + info[i + j]
    j = j + 1
debug.write(user4 + "\t")
print("user4 = "+ user4)


url = "WEBHOOKS_URL"
file = open('INFO_PATH', 'r+')
info = file.read()
file.close
file = open('INFO_PATH', 'w+')
out = ''

if (user1 == "Not authorized"):
    out = out + info[0]
elif (user1 != "null"):
    out = out + "1"
    if (info[0] == '0'):
        data = {
            "content" : "user1: "+user1,
            "username" : "Place42"
        }
        requests.post(url, json = data)
else:
    out = out + "0"

if (user2 == "Not authorized"):
    out = out + info[1]
elif (user2 != "null"):
    out = out + "1"
    if (info[1] == '0'):
        data = {
            "content" : "user2: "+user2,
            "username" : "Place42"
        }
        requests.post(url, json = data)
else:
    out = out + "0"

if (user3 == "Not authorized"):
    out = out + info[2]
elif (user3 != "null"):
    out = out + "1"
    if (info[2] == '0'):
        data = {
            "content" : "user3: "+user3,
            "username" : "Place42"
        }
        requests.post(url, json = data)
else:
    out = out + "0"

if (user4 == "Not authorized"):
    out = out + info[3]
elif (user4 != "null"):
    out = out + "1"
    if (info[3] == '0'):
        data = {
            "content" : "user4tor: "+user4,
            "username" : "Place42"
        }
        requests.post(url, json = data)
else:
    out = out + "0"
print(out)
file.write(out)
debug.write(out + "\tok\n")