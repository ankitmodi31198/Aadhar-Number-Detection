import pytesseract
# from PIL import Image
import cv2 as cv

# img = Image.open('text.png')
img = cv.imread('download.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)
t = ""
with open('download.txt', mode='w') as file:
    for r in result:
        if r.isdigit():
            t = t+r
    s=len(t)
    t = t[s-12:]
    file.write(t)
    print('got success')

file.close()