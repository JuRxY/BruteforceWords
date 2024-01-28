import os
import cv2
import numpy as np
import tensorflow as tf
from keras import layers, models
from sklearn.model_selection import train_test_split

# Function to load and preprocess the dataset
def load_dataset(dataset_path):
    images = []
    labels = []

    # Define a string of all valid characters (A-Ž)
    valid_chars = 'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".png"):  # Assuming images are in PNG format
                image_path = os.path.join(root, file)
                # Check if the first character of the filename is in valid_chars
                if file[0].upper() in valid_chars:
                    label = valid_chars.index(file[0].upper())  # Use the index of the character in valid_chars as the label
                    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    if img is not None:
                        img = cv2.resize(img, (94, 94))  # Resize images to a standard size

                        images.append(img)
                        labels.append(label)

    images = np.array(images) / 255.0  # Normalize pixel values to the range [0, 1]
    labels = np.array(labels)

    return images, labels

# Load and preprocess the dataset
dataset_path = './crke/'
images, labels = load_dataset(dataset_path)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Define the CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(94, 94, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(26, activation='softmax'))  # Output layer with 26 classes (A-Z)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train.reshape(-1, 94, 94, 1), y_train, epochs=10, validation_data=(X_test.reshape(-1, 94, 94, 1), y_test))

# Save the trained model
model.save('./model.keras')
