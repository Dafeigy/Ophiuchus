from flask import Flask, Response, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import encoder
import sampler
import json

# Check if the "upload" directory exists in the project root
upload_dir = os.path.join(os.getcwd(), "upload")
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_dir  # 设置上传文件夹的保存路径

@app.route("/data")
def update_qrcode():
    global data_source, data_stream_generator
    
    return next(data_stream_generator)

@app.route("/")
def main():
    entries = os.listdir(upload_dir)
    return render_template("index.html", entries=entries)
   
@app.route('/upload', methods=['POST'])
def upload_file():
    global data_source, data_stream_generator
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename, buffer_size=266144)
        lteconder = encoder.LTEncoder(32, filename)
        data_stream_generator = lteconder._gen_blocks()
        return jsonify({'success': 'File uploaded successfully'}), 200

if __name__ == '__main__':
    app.run("0.0.0.0", 3000, debug=True)
