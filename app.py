import os
#import magic
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from lane import lane_interface
from traffic_sign import sign_interface

UPLOAD_FOLDER_LANE = 'C:/Users/Esoundarajan/Desktop/Elango/Personal/DBS/Adithya_Chowdary/Lane_Detection_Code/input'
UPLOAD_FOLDER_SIGN = 'C:/Users/Esoundarajan/Desktop/Elango/Personal/DBS/Adithya_Chowdary/Lane_Detection_Code/static/sign_input'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER_LANE'] = UPLOAD_FOLDER_LANE
app.config['UPLOAD_FOLDER_SIGN'] = UPLOAD_FOLDER_SIGN
app.secret_key = "secret key"


@app.route('/')
def index():
    return redirect('/lane')

@app.route('/lane')
def lane():
    return render_template('lane.html')

@app.route('/traffic_sign')
def traffic_sign():
    return render_template('traffic_sign.html')

@app.route('/uploadlaneinputimage',methods=['GET','POST'])
def upload_file_lane():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_LANE'], filename))
            flash('File successfully uploaded')
            return lane_interface.executemodel(filename)
            #return redirect('/')
        else:
            flash('Allowed file types are jpg, jpeg')
            return redirect(request.url)

@app.route('/uploadsigninputimage',methods=['GET','POST'])
def upload_file_sign():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_SIGN'], filename))
            flash('File successfully uploaded')
            return sign_interface.executemodel(filename)
            #return redirect('/')
        else:
            flash('Allowed file types are jpg, jpeg')
            return redirect(request.url)

if __name__ == "__main__":
    app.debug = True
    app.run()