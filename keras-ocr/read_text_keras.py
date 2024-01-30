import keras_ocr
import pyautogui
import numpy as np
import cv2

# Get a set of three pre-trained models
pipeline = keras_ocr.pipeline.Pipeline()

# Get a screenshot
screenshot = pyautogui.screenshot()

# Convert the screenshot to a NumPy array and normalize pixel values to the range [0, 1]
screenshot_np = np.array(screenshot)


lower = np.array([59-10, 65-10, 108-10])
upper = np.array([59+10, 65+10, 108+10])

# Apply a mask to keep only the pixels that match the color of the letters
mask = cv2.inRange(screenshot_np, lower, upper)

# Apply the mask to the original screenshot to get a color image that only includes the letters
masked_screenshot = cv2.bitwise_and(screenshot_np, screenshot_np, mask=mask)

cv2.imshow('masked_screenshot', cv2.resize(masked_screenshot, (960, 540)))
cv2.waitKey(0)
cv2.destroyAllWindows()

#! PREPROCESSING
# Define a kernel for the dilation operation
kernel = np.ones((5,5),np.uint8)

# Dilate the masked screenshot to make the text thicker
dilated_screenshot = cv2.dilate(masked_screenshot, kernel, iterations = 1)

# Use the models to detect and recognize text in the dilated screenshot
# prediction_groups = pipeline.recognize([dilated_screenshot])


#! PREDICT
prediction_groups = pipeline.recognize([masked_screenshot])

# Draw the bounding boxes
for prediction_group in prediction_groups:
    for word, box in prediction_group:
        print(word)
        top_left = tuple(box[0].astype(int))
        bottom_right = tuple(box[2].astype(int))
        screenshot_np = cv2.rectangle(screenshot_np, top_left, bottom_right, (0, 255, 0), 2)

# Define the size of the window
window_size = (960, 540)  # Example values

# Resize the screenshot
screenshot_resized = cv2.resize(screenshot_np, window_size)

# Display the resized screenshot
cv2.imshow('screenshot', cv2.cvtColor(screenshot_resized, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()