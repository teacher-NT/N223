import os
os.system("cls")

car = {
    "brand": "BMW",
    "model": "M3",
    "price": 120_000,
    "color": "blue",
    "milage": 50_000,
    "model": "Damas"
}

car['year'] = 2022

# car["model"] = "M5 Compitetion"
# print(car)
# print(car['brand'])
# print(car['color'])
# print(car['model'])

# if "model" in car:
#     print("Bor")
# else:
#     print("Yo'q")

# for i in car:
#     print(i, car[i])

# =========================================

salon = {
    "GM Matiz": {
        "price": 5000,
        "year": [2023, 2019, 2015],
        "colors": ['white', 'black', 'green', 'blue']
    },
    "GM Nexia": {
            "price": 9000,
            "year": 2021,
            "colors": ['white', 'black',]
        },
    "GM Cobalt": {
            "price": 13000,
            "year": 2024,
            "colors": ['white', 'black', 'green']
        }
}

# print(salon["GM Matiz"]['colors'][1])
# =============================================================

student = {
    "name": 'Ali',
    "surname": "Valiev",
    "age": 21,
    "address": "Toshkent"
}
# print(student.get('name', 'Kalit topilmadi'))
# print(student['ism'])

keys = list(student.keys())
# print(keys)

values = list(student.values())
# print(values)
# if "Toshkent" in values:
#     print("Bor")
# else:
#     print("Yo'q")

# n = student.pop('surname')
# print(student)
# print(n)

# m = student.popitem()
# print(m)
# print(student)

# items = student.items()
# print(items)
# for i in student:
#     print(i, student[i])
# for k, v in student.items():
#     print(k, v)

# student['age'] = 30
# student['address'] = 'Xorazm'
# student['surname'] = 'Hasanov'

student.update({"age": 30, 'address':'Xorazm', 'surname':'Hasanov'})
print(student)