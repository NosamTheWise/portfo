from flask import Flask, render_template, send_from_directory, request, redirect
import os
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f'\n{email}\n{subject}\n{message}\n')

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csv_writer=csv_writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE.MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
   	    return 'Something went wrong, please try again.'