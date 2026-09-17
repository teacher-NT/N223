import os
os.system("cls")

import cv2

camera = cv2.VideoCapture(0)
while True:
    is_valid, image = camera.read()
    if is_valid:
        cv2.imshow("Kamera", image)
    else:
        print("Tasvirni o'qishda xatolik")
    if cv2.waitKey(1) & 0xfff == 32:
        break