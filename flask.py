from flask import Flask, request, jsonify
from PIL import Image
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Read the image from the uploaded file
    image_bytes = file.read()  # Get the image as byte stream
    
    # Convert byte stream to an in-memory image object (Pillow)
    image = Image.open(io.BytesIO(image_bytes))
    
    # Perform greyscaling with OpenCV (convert to NumPy array)
    greyscaled_image = greyscale_with_opencv(image)

    # Perform cropping with Pillow
    cropped_image = crop_with_pillow(image, (100, 100, 400, 400))

    # Return response (for demonstration)
    return jsonify({"message": "Image processed successfully"})

def greyscale_with_opencv(image):
    # Convert from Pillow Image to OpenCV format (NumPy array)
    image_cv = np.array(image)
    # Convert from RGB (Pillow) to BGR (OpenCV)
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_RGB2BGR)
    
    # Apply greyscaling with OpenCV
    greyscale_img = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    return greyscale_img

def crop_with_pillow(image, coordinates):
    # Crop the image using Pillow
    cropped_img = image.crop(coordinates)
    return cropped_img

if __name__ == '__main__':
    app.run(debug=True)
