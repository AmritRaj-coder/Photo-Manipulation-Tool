from flask import Flask, render_template, request, send_file
from PIL import Image, ImageOps
import io
import os

app = Flask(__name__)

# Home page with upload form
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle image upload and manipulation
@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No image uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    action = request.form.get('action', 'grayscale')
    image = Image.open(file.stream)

    # Apply transformations
    if action == 'grayscale':
        image = ImageOps.grayscale(image)
    elif action == 'invert':
        image = ImageOps.invert(image.convert('RGB'))
    elif action == 'rotate':
        image = image.rotate(90, expand=True)

    # Save to BytesIO and send to browser
    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
