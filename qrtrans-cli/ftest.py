from flask import Flask,Response,render_template,request
from werkzeug.utils import secure_filename
import os
import encoder
import sampler
import json
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'  # 设置上传文件夹的保存路径

data_source = "hello woroksdja osiu ahsdiuahsoiduhaksj basidhal hjklasdhklja jklh"

lteconder = encoder.LTEncoder(32, data_source)
data_stream_generator = lteconder._gen_blocks(data_source)

@app.route("/data")
def update_qrcode():
    return next(data_stream_generator)

@app.route("/")
def main():
    entries = os.listdir("./upload")
    return render_template("index.html", entries=entries)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   
   if request.method == 'POST':
      f = request.files['file-select']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
      return f'file {f.filename} uploaded successfully'
app.run(debug = True)



if __name__ == '__main__':
    app.run("192.168.137.1",5000, debug=True)

