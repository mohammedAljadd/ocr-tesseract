import cv2
import pytesseract

# font for drawing bounding boxes
font = cv2.FONT_HERSHEY_SIMPLEX

# tesseract software (you have to install it)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# load the image
img = cv2.imread("img.png")
img = cv2.resize(img, (960, 540)) 

# by default, cv2 shows images in BGR format. We want the images in RGB format.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# result of prediction:
predictions = pytesseract.image_to_string(img)

# Bounding boxes (string)
result = pytesseract.image_to_boxes(img)

# Drawing the bounding boxes
result_as_array = result.split("\n")

for i in range(0, len(result_as_array)-1):
    result_as_array[i] = result_as_array[i].split(" ")

hIMG, wIMG, channel = img.shape

for i in range(0, len(result_as_array)-1):
    x1, y1, x2, y2 = int(result_as_array[i][1]), int(result_as_array[i][2]), int(result_as_array[i][3]), int(result_as_array[i][4])
    cv2.rectangle(img, (x1, hIMG-y1), (x2, hIMG-y2), (0,0,255), 1)

# labeling each boxes

for i in range(0, len(result_as_array)-1):
    x1, y1, x2, y2 = int(result_as_array[i][1]), int(result_as_array[i][2]), int(result_as_array[i][3]), int(result_as_array[i][4])
    wBOX = x2 - x1
    hBOX = y2 - y1
    xLocationOfLabel = int(x1 + wBOX/3)
    print(xLocationOfLabel)
    character = result_as_array[i][0]
    cv2.putText(img,
              character,
              (xLocationOfLabel,hIMG-y1-hBOX),
              font, 1,
              (255, 0, 0),
              1,
              cv2.LINE_4)

cv2.imshow('OCR result', img)
cv2.waitKey(0)

