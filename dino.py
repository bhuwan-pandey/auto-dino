import pyautogui
import time
from mss import mss
from PIL import Image


y = obj =  None
# bg_white = (255, 255, 255)
# bg_black = (0, 0, 0)
# obj_white = (172, 172, 172)
# obj_black = (83, 83, 83)
running = True
img = None

time.sleep(3)


while running:
    while running:
        with mss() as shot:
            mon = shot.monitors[1]
            img = shot.grab(mon)
            img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
            # crop_rectangle = (475, 200, 550, 230)  # left upper right lower
            crop_rectangle = (720, 285, 825, 325)  # left upper right lower
            cropped_img = img.crop(crop_rectangle)
            width, height = cropped_img.size
            pixels = cropped_img.load()
            # obj = obj_black if pixels[0, 0] == bg_white else obj_white
            for x in range(0, height):
                for y in range(0, width):
                    # print(pixels[y,x])
                    if pixels[y, x] != pixels[0,0]:
                        pyautogui.typewrite(' ')
                        break
                if pixels[y, x] != pixels[0,0]:
                    break
