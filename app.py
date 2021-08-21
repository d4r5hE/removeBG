import json
import os

from flask import Flask, jsonify, request
from inference import BGRemove

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the flask API"

@app.route('/bgremove',methods=['POST'])
def remove_bg():
    file = request.files['image']
    os.makedirs(os.path.join(app.instance_path, 'uploaded_image'), exist_ok=True)
    file.save(os.path.join(app.instance_path, 'uploaded_image', file.filename))
    saved_file = os.path.join(app.instance_path, 'uploaded_image', file.filename)
    bg = BGRemove("pretrained/modnet_photographic_portrait_matting.ckpt")
    output_file = bg.image(saved_file)
    return jsonify({'filename': output_file})

if __name__ == "__main__":
    app.run(debug=True)
