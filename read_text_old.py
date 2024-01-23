import pyautogui
import easyocr
import numpy as np

def extract_text_from_screenshot():
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the PIL.Image object to a numpy array
    screenshot_np = np.array(screenshot)

    # Use easyocr to perform OCR on the image
    reader = easyocr.Reader(['en'])
    text_results = reader.readtext(screenshot_np)
    

    # Extract text from the results
    extracted_text = [result[1] for result in text_results]

    return extracted_text

if __name__ == "__main__":
    try:
        text_found = extract_text_from_screenshot()
        if text_found:
            print(text_found)
        else:
            print("No text found on the screen.")
    except Exception as e:
        print(f"Error: {e}")

    
    #pos = words.generate_possibilities("rkao")
    #print(pos)

