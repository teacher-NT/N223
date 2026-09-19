
import os
os.system("cls")

import json

with open("students.json") as file:
    students = json.load(file)

print(students[2])