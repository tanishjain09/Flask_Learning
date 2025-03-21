from fileinput import filename
from http.client import responses

import os
import uuid
import pandas as pd
from flask import Flask,render_template,redirect,url_for,request,Response,send_from_directory,jsonify

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
      return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'neuralnine' and password == 'password':
            return "Success"
        else:
            return "Failure"

@app.route('/file_upload',methods = ['POST'])
def file_upload():
    if 'file' not in request.files:
        return "No file part in the request"
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()

@app.route('/convert_csv',methods = ['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(index=False),  # Convert DataFrame to CSV
        mimetype='text/csv',  # Corrected parameter name (mimetype instead of mimetypes)
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response

@app.route('/convert_csv_two',methods = ['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename),encoding='utf-8')
    return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name = 'result.csv')


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)