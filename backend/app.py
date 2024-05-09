from tensorflow.keras.preprocessing.image import ImageDataGenerator
from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pickle
import shutil
import os
import cv2
from io import BytesIO

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

test_datagen = ImageDataGenerator(rescale=1./255)
class_labels = {0: 'non-vehicle', 1: 'vehicle'}

def visualize_predictions(model, test_data_gen):
    # Generate predictions for the test set
    predictions = model.predict(test_data_gen)
    
    # Get the true labels from the test set
    true_labels = test_data_gen.classes

    filenames = test_data_gen.filenames

    # # # Select a random sample of test images
    sample_indices = range(len(filenames))

    # # Display the images with predictions
    for i in sample_indices:
        filename = filenames[i]

    #     # Get the true label
        true_label = class_labels[true_labels[i]]
        print('true_label',true_label)

    #     # Get the predicted probability and class
        predicted_prob = predictions[i]
        predicted_class = int(predicted_prob > 0.5)
        predicted_label = class_labels[predicted_class]

        # Determine the color for the label (green for correct, red for incorrect)
        label_color = 'green' if true_label == predicted_label else 'red'

        # # Load and display the image
        img_path = os.path.join('test_folder', filename)
        img = plt.imread(img_path)

        plt.imshow(img)
        plt.title(f'True: {true_label}, Predicted: {predicted_label}', color=label_color)
        plt.axis('off')
        plt.show()

@app.route('/api/detect', methods=['POST'])
def predict():
    if 'test_file' not in request.files:
        print("No file uploaded")
        return jsonify({'error': 'No file uploaded'})

    files = request.files.getlist('test_file')

    if len(files) == 0:
        return jsonify({'error': 'No files selected'})
    
    if not os.path.exists('test_folder/test_imgs'):
        os.makedirs('test_folder/test_imgs')
    num_files= len(files)
    for file in files:
        if file:
            file_path = os.path.join('test_folder/test_imgs', file.filename)
            file.save(file_path)
            print(f"File '{file.filename}' uploaded")

            # Load images using the data generator
            test_image_generator = test_datagen.flow_from_directory(
                'test_folder',
                target_size=(64, 64),
                batch_size=32,
                class_mode='binary',
                shuffle=False
            )
            visualize_predictions(model, test_image_generator)
            # Delete the file
            os.remove(file_path)

        else:
            print("Error uploading file")
            return jsonify({'error': 'Error uploading file'})
    

    # return send_file(img_buffer, mimetype='image/png')
    return "File uploaded successfully"

    
if __name__ == '__main__':
    app.run(debug=True)