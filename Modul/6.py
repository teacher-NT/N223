import os
os.system("cls")

import wikipedia as wk
wk.set_lang("uz")

page = wk.page("Cristiano Ronaldo")
# print(page.content)
print(page.summary)