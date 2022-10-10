import cv2
from PIL import Image
from pytesseract import pytesseract
def tesseract():
    path_to_tesseract = (r"C:\\Users\\my pc\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe")
    image_path = "test1.jpg"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])
camera=cv2.VideoCapture(0)
while True:
    _,image=camera.read()
    cv2.imshow('image',image)
    if cv2.waitKey(1)& 0xFF==ord('s' or 'S'):
        cv2.imwrite('test1.jpg',image)
        tesseract()
    elif cv2.waitKey(1)& 0xFF==ord('q' or 'Q'):
        cv2.destroyAllWindows()
        break
camera.release()
cv2.destroyAllWindows()