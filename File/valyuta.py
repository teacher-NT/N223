import os
os.system("cls")

import json
import requests as rq

link = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

data = rq.get(link)
data = data.json()

print(float(data[0]['Rate'])*25)