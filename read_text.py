import numpy as np
import cv2
import os

def get_files_in_directory(directory_path):
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return files

def is_far_enough(point, points, min_distance):
    return all(np.linalg.norm(np.array(point) - np.array(p)) >= min_distance for p in points)

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "letters/levels/alps.jpg")

    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresholded = cv2.threshold(gray, 21, 255, cv2.THRESH_BINARY_INV)
    black_pixels = np.where(thresholded == 255)

    black_pixels_list = list(zip(black_pixels[1], black_pixels[0]))

    min_distance = 100  # Minimum distance between pixels
    filtered_pixels = []

    for p in black_pixels_list:
        if is_far_enough(p, filtered_pixels, min_distance):
            filtered_pixels.append(p)

    print(filtered_pixels)