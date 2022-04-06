#importing opencv and pytesseract
import cv2
import pytesseract

def ocr_process():
	img = cv2.imread("images/1.png")
	#Resize the image
	# img = cv2.resize(img, None, fx=0.5, fy=0.5)
	#Convert image to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#Convert image to black and white
	new_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

	# new_image = cv2.GaussianBlur(img,(5,5),0)
	# new_image_ret,new_image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	cv2.imwrite("saved.png", new_image)

	text = pytesseract.image_to_string(new_image, config="--psm 3")
	print(text)

if __name__ == "__main__":
	ocr_process()
