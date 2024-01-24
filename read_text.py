import pyautogui
import easyocr
import numpy as np
import words

def cleanup_text(text):
    return "".join([c if c.isalpha() else "" for c in text]).strip()

def extract_text_from_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    # Easyocr
    reader = easyocr.Reader(['sl'])
    text_results = reader.readtext(screenshot_np, width_ths=2, height_ths=0.1)  # tweakat je treba te parametre

    text_list = []  # [(crka: str, (x, y): tuple)]
    for (bbox, text, prob) in text_results:
        (tl, tr, br, bl) = bbox     # top left, top right, bottom right, bottom left
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        text = cleanup_text(text)
        if text == "5": text = "S"  # iz nekega razloga easyocr ne zna prebrt S u tem fontu
        if text == "1": text = "I"
        if len(text) != 0 and len(text) < 3: text_list.append((text, (int((tl[0] + br[0])/2), int((tl[1] + br[1])/2))))  # sori za tole ampak znajd se ;)
    
    return text_list

res = extract_text_from_screenshot()
print(res)