import os
os.system("cls")

# set1 = {90,20,34,50,16,2,20,50,16}
# print(set1)
# print(set1[2]) error
# set1[2] = 25 error
# ===================================================

# myset = {55,44,66,33,77,22,88}
# for i in myset:
#     print(i, end=" ")

# fruits = {"olma", 'anor', 'gilos', 'banan', 'shaftoli'}
# print()

# if 'anor' in fruits:
#     print("Bor")
# else:
#     print("Yo'q")
# =====================================================


myset2 = {90,80,70,60,50}

# myset2.add(10)
# print(myset2)

# myset2.remove(60)
# print(myset2)

# myset2.discard(20)
# print(myset2)

# n = myset2.pop()
# print(myset2)
# print(n)

# myset2.clear()
# print(myset2)

# myset3 = myset2.copy()
# print(myset2)
# print(myset3)

# mylist = [1,10,20,30,60,50]
# myset2.update(mylist)
# print(myset2)

# mylist = [1,10,20,30,60,50]
# myset3 = myset2.union(mylist)
# print(myset2)
# print(myset3)



set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2)
# print(set3)

# set4 = set2.difference(set1)
# print(set4)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)

# sonlar1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# sonlar2 = {5,6,7,8,9}

# print(sonlar1.issubset(sonlar2))
# print(sonlar2.issubset(sonlar1))

# print(sonlar1.issuperset(sonlar2))
# print(sonlar2.issuperset(sonlar1))
