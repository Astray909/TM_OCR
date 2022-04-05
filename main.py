from PIL import Image
import pytesseract
import numpy as np


import cv2

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


def ocr_load(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)
    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    out_below = pytesseract.image_to_string(img)
    print("OUTPUT:", out_below)

if __name__ == "__main__":
    ocr_load("/mnt/c/Users/jhuang/Desktop/1.png")