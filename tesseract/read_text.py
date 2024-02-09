# https://github.com/tesseract-ocr/tessdata/blob/main/slv.traineddata
# https://github.com/UB-Mannheim/tesseract/wiki

import pytesseract
import pyautogui
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"   # Zamenjej za svojo pot do tesseract.exe lah installas na:
                                                                            # https://github.com/UB-Mannheim/tesseract/wiki

img = pyautogui.screenshot()
img = np.array(img)
img_original = img.copy()

#! PREPROCESSING

lower = np.array([59-10, 65-10, 108-10])
upper = np.array([59+10, 65+10, 108+10])

mask = cv2.inRange(img, lower, upper)
img = cv2.bitwise_and(img, img, mask=mask)  # dejansko maskira stvari, ki so izven barvnega spektra

kernel = np.ones((3,3), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img = cv2.erode(img, kernel, iterations=3)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)


#? cv2.imshow("masked", cv2.resize(img, (960, 540)))


#! RECOGNITION
boxes = pytesseract.image_to_boxes(
    img, 
    config="-c tessedit_char_whitelist=abcčdefghijklmnoprsštuvzžABCČDEFGHIJKLMNOPRSŠTUVZŽ0123456789 --psm 6",
    lang="slv"
)

# Get the dimensions of the image
height, width, _ = img_original.shape

# Parse the boxes string
lines = boxes.split('\n')
for line in lines:
    parts = line.split(' ')
    if len(parts) >= 6:
        char = parts[0]
        x1 = int(parts[1])
        y1 = height - int(parts[2])  # Adjust the y-coordinate
        x2 = int(parts[3])
        y2 = height - int(parts[4])  # Adjust the y-coordinate
        # BB
        cv2.rectangle(img_original, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # CHAR
        cv2.putText(img_original, char, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#? cv2.imshow('screenshot', cv2.cvtColor(cv2.resize(img_original, (960, 540)), cv2.COLOR_BGR2RGB))
#? cv2.waitKey(0)
#? cv2.destroyAllWindows()