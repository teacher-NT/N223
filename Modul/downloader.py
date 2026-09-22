#  pip install pytubefix
import os
os.system("cls")

from pytubefix import YouTube

link = input("Video linkini kiriting: ")

try:
    print("Ulanmoqda...")
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    print("Video yuklanmoqda...")
    video.download(".")
except Exception as e:
    print("Nimadir xato ketdi...", e)
else:
    print("Yuklash yakunlandi...")