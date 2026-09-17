import os
os.system("cls")

from translate import Translator

tarjimon = Translator(to_lang="tr", from_lang="uz")

text = input("Matn kiriting: ")
text = tarjimon.translate(text)
print(text)