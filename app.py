from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from preprocess import img_to_text, resized_image
import base64

 
app = Flask(__name__)
 
@app.route('/')

@app.route("/index")
def home():
    Text=''
    Text = img_to_text(r"static\\uploads\\1.jpg")
    return render_template("index.html", Text=Text)
    

UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print(allowed_file)
 
@app.route('/uploader', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename="1.jpg"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        Text = img_to_text(r"static\\uploads\\1.jpg")
        resized_image(r"static\\uploads\\1.jpg")
        PIC_FOLDER = os.path.join(r'static', 'uploads')
        app.config['UPLOAD_FOLDER'] = PIC_FOLDER
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '2.jpg')
        return render_template('result.html', filename=filename , Text=Text, img=full_filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    #return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.debug = True
    app.run()