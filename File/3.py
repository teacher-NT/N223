
import os
os.system("cls")

import json

students = [
    {
        "name": "Shaxboz",
        "age": 15,
        "address": "Olmaliq"
    },
    {
        "name": "Azizbek",
        "age": 18,
        "address": "Qo'qon"
    },
    {
        "name": "Zayniddin",
        "age": 18,
        "address": "Qashqadaryo"
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
    print("Faylga yozildi")