import words
import tesseract.read_text as read_text
import pyautogui
import time

amout_of_levels = 1

while amout_of_levels:
    letters = read_text.get_letter_coordinates()    #[(char1, (x1, y1)), (char2, (x2, y2)), ...]
    word = ""
    for i, (char, _) in enumerate(letters):
        word += char
    
    words_list = words.generate_possibilities(word)  #[word1, word2, ...]
    for word in words_list:
        for i, letter in enumerate(word):
            for char, coords in letters:
                if char.lower() == letter.lower():
                    if i == 0:
                        pyautogui.mouseDown(*coords)
                    elif i == len(word) - 1:
                        pyautogui.moveTo(*coords)
                        pyautogui.mouseUp()
                    else:
                        pyautogui.moveTo(*coords)
                    time.sleep(0.1)
    if amout_of_levels == True:
        pass
    if isinstance(amout_of_levels, int):
        amout_of_levels -= 1