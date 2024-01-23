import pyautogui
import os
import cv2
import numpy as np
import imutils

def get_files_in_directory(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "letters")
    letter_pngs = get_files_in_directory(path)
    # print(letter_pngs)
    pyautogui.screenshot().save("_.png")

    for letter in letter_pngs:
        result = pyautogui.locateCenterOnScreen(os.path.join(path, letter), confidence=0.8, grayscale=True)
        print(result)
        