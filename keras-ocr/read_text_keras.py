import keras_ocr
import pyautogui
import numpy as np
import cv2

# Get a set of three pre-trained models
pipeline = keras_ocr.pipeline.Pipeline()

# Get a screenshot
screenshot = pyautogui.screenshot()

# Convert the screenshot to a NumPy array and normalize pixel values to the range [0, 1]
screenshot_np = (np.array(screenshot) / 255.0 * 255).astype(np.uint8)
# cv2.imshow('screenshot', screenshot_np)
# cv2.waitKey(0)

# Use the models to detect and recognize text in the screenshot
prediction_groups = pipeline.recognize([screenshot_np])

screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

# Draw the bounding boxes
for prediction_group in prediction_groups:
    for word, box in prediction_group:
        top_left = tuple(box[0].astype(int))
        bottom_right = tuple(box[2].astype(int))
        screenshot_rgb = cv2.rectangle(screenshot_rgb, top_left, bottom_right, (0, 255, 0), 2)


# Define the size of the window
window_size = (960, 540)  # Example values

# Resize the screenshot
screenshot_resized = cv2.resize(screenshot_rgb, window_size)

# Display the resized screenshot
cv2.imshow('screenshot', screenshot_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()