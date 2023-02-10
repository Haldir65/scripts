from flask import Flask
import os
from flask import Flask, flash, request, redirect, url_for,abort
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'resources'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','zip'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),UPLOAD_FOLDER)


@app.route('/')
def index():
    return 'Index Page 222'

@app.route('/hello')
def hello():
    return 'Hello, World'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    

@app.route('/file_save',methods = ['GET','POST'])
def _save_file():
    if request.method == 'POST':
        try:
            if not request.files:
                return abort(403,'missing required params file')
            if 'file' not in request.files:
                print("file missing")
                flash('No file part')
                return redirect(request.url)    
            if not 'authority' in request.headers:
                print("authority missing")
                return abort(403,'unauthorized request')
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            # create the folders when setting up your app
            if file and allowed_file(file.filename):
                dirname = app.config['UPLOAD_FOLDER']
                os.makedirs(dirname, exist_ok=True)
                # when saving the file
                abs_fpath = os.path.join(dirname, secure_filename(file.filename))
                # print(abs_fpath)
                file.save(abs_fpath)            
        except Exception as e:
            print(str(e))
            return 'some error happend when attempting to save file {0} '.format(str(e))
    return 'file uploaded successfully'



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True )    