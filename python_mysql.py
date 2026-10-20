import os
os.system("cls")

from mysql import connector

mydb = connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database='dars_db'
)
# print(mydb)
# print("Serverga ulandi...")

cursor = mydb.cursor()

# cursor.execute("SHOW DATABASES;")
# for i in cursor:
#     print(i)

# cursor.execute("SELECT * FROM students;")

# jadval = cursor.fetchall()
# for i in jadval:
#     print(i)

# qator = cursor.fetchone()
# print(qator)

# qatorlar = cursor.fetchmany(3)
# for i in qatorlar:
#     print(i)


# QUERY = """INSERT INTO students(name, lastname, birthdate, faculty, grade, stipendiya)
#     VALUES
#     ('Azizbek', 'Muhammadjonov', '2008-07-21', 'Data Science', 1, 610000);
# """
# cursor.execute(QUERY)
# mydb.commit()
# print(f"{cursor.rowcount} ta qator")

ism = input("Ism: ")
fam = input("Familya: ")
ts = input("Tug'ilgan sana: ")
fak = input("Fakultet: ")
gra = int(input("Bosqich: "))
stip = float(input("Stipendiya: "))
QUERY2 = """INSERT INTO students(name, lastname, birthdate, faculty, grade, stipendiya)
    VALUES
    (%s, %s, %s, %s, %s, %s);
"""
cursor.execute(QUERY2, (ism,fam, ts,fak,gra,stip))
mydb.commit()
print(f"{cursor.rowcount} ta qator")
