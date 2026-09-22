#  pip install pytubefix
import os
os.system("cls")

# from pytubefix import YouTube
# from pytubefix.cli import on_progress

# link = input("Video linkini kiriting: ")

# try:
#     print("Ulanmoqda...")
#     # yt = YouTube(link)
#     yt = YouTube(link, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
#     video = yt.streams.get_highest_resolution()
#     print("Video yuklanmoqda...")
#     video.download()
# except Exception as e:
#     print("Nimadir xato ketdi...", e)
# else:
#     print("Yuklash yakunlandi...")



import yt_dlp

url = input("Video linkini kiriting: ")
ydl_opts = {}
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Jarayon boshlandi...")
        ydl.download([url])
except:
    print("XAtolik sodir bol'di")
else:
    print("Video yuklandi...")
