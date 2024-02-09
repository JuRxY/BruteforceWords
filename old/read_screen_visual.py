import pyautogui
import easyocr
import numpy as np
import cv2
import words

def cleanup_text(text):
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def extract_text_from_screenshot():
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)    # dela kerkol image ka je np array

    # Easyocr
    reader = easyocr.Reader(['sl'])
    text_results = reader.readtext(screenshot_np, width_ths=2, height_ths=0.1)   # screenshot_np (more bit np array)
    

    return (text_results, screenshot_np)

def visualise_results():
    try:
        (results, image) = extract_text_from_screenshot()
        text_list = []
        for (bbox, text, prob) in results:
            # Unpackam bounding box
            (tl, tr, br, bl) = bbox     # top left, top right, bottom right, bottom left
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))

            text = cleanup_text(text)
            if text == "5": text = "S"
            text_list.append(text)
            cv2.rectangle(image, tl, br, (0, 255, 0), 2)
            cv2.putText(image, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        return (cv2.resize(image, (image.shape[1]//2, image.shape[0]//2)), text_list)  #! ignorej to tle sam resizam image da fitta na screen


    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    (image, text_list) = visualise_results()
    cv2.imshow("Image", image)  #! ignorej to tle sam resizam image da fitta na screen
    cv2.waitKey(0)

    
    #pos = words.generate_possibilities("".join(text_list))
    #print(pos)

