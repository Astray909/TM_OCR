from PIL import Image
import pytesseract
import numpy as np

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


def ocr_load(filename):
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)
    print(text)

if __name__ == "__main__":
    ocr_load("/mnt/c/Users/jhuang/Desktop/0_yiPwbeVpiriPJzLw.jpeg")