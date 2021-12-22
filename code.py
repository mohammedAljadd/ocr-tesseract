import cv2
import pytesseract

# font for drawing bounding boxes
font = cv2.FONT_HERSHEY_SIMPLEX

# tesseract software (you have to install it)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# load the image
img = cv2.imread("img.png")

# by default, cv2 shows images in BGR format. We want the images in RGB format.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# result of prediction:
predictions = pytesseract.image_to_string(img)

print(predictions)

cv2.imshow('OCR result', img)
cv2.waitKey(0)

