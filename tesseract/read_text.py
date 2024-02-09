# https://github.com/tesseract-ocr/tessdata/blob/main/slv.traineddata
# https://github.com/UB-Mannheim/tesseract/wiki

import pytesseract
import pyautogui
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"   # Zamenjej za svojo pot do tesseract.exe lah installas na:
                                                                            # https://github.com/UB-Mannheim/tesseract/wiki

def get_letter_coordinates():
    img = pyautogui.screenshot()
    img = np.array(img)
    img_original = img.copy()

    lower = np.array([59-10, 65-10, 108-10])
    upper = np.array([59+10, 65+10, 108+10])

    mask = cv2.inRange(img, lower, upper)
    img = cv2.bitwise_and(img, img, mask=mask)

    kernel = np.ones((3,3), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.erode(img, kernel, iterations=3)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    boxes = pytesseract.image_to_boxes(
        img, 
        config="-c tessedit_char_whitelist=abcčdefghijklmnoprsštuvzžABCČDEFGHIJKLMNOPRSŠTUVZŽ0123456789 --psm 6",
        lang="slv"
    )

    height, width, _ = img_original.shape

    letter_coordinates = []
    lines = boxes.split('\n')
    for line in lines:
        parts = line.split(' ')
        if len(parts) >= 6:
            char = parts[0]
            x1 = int(parts[1])
            y1 = height - int(parts[2])
            x2 = int(parts[3])
            y2 = height - int(parts[4])

            # BB center
            x_center = (x1 + x2) // 2
            y_center = (y1 + y2) // 2

            letter_coordinates.append((char.lower(), (x_center, y_center)))

    return letter_coordinates

# out = get_letter_coordinates()
# print(out)