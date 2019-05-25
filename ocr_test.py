from PIL import Image
import pytesseract
import cv2

image = Image.open('test.jpg')
print(image)
print(pytesseract.image_to_string(image))

img = cv2.imread('test.jpg')
print(pytesseract.image_to_string(img))
