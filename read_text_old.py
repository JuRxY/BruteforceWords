import pyautogui
import easyocr
import numpy as np
import cv2

def cleanup_text(text):
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def extract_text_from_screenshot():
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot.save("_temp.png")
    screenshot_np = np.array(screenshot)
    image = cv2.imread("./letters/levels/alps.jpg") # temporary -> pousod kjer je image more bit screenshot_np

    # Easyocr
    reader = easyocr.Reader(['sl'], gpu="cuda:0")   #! samo za cuda compatible GPU
    text_results = reader.readtext(image)   # screenshot_np (more bit np array)
    

    # Extract text from the results
    # extracted_text = [result[1] for result in text_results]

    return (text_results, image)

if __name__ == "__main__":
    try:
        (results, image) = extract_text_from_screenshot()
        for (bbox, text, prob) in results:
            # Unpackam bounding box
            (tl, tr, br, bl) = bbox     # top left, top right, bottom right, bottom left
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))

            text = cleanup_text(text)
            cv2.rectangle(image, tl, br, (0, 255, 0), 2)
            cv2.putText(image, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        
        cv2.imshow("Image", cv2.resize(image, (image.shape[1]//3, image.shape[0]//3)))  #! ignorej to tle sam resizam image da fitta na screen
        cv2.waitKey(0)

    except Exception as e:
        print(f"Error: {e}")

    
    #pos = words.generate_possibilities("rkao")
    #print(pos)

