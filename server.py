from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/<string:html_page>")
def a_page(html_page):
    return render_template(html_page)

colm = ['name', 'email', 'message']

try:
    with open('database.csv', mode='w') as database:
        csvwriter = csv.writer(database)
        csvwriter.writerow(colm)
except:
    pass

def csv_file_writer(data):
    data = [data]
    with open('database.csv', mode='a') as database:
        writer = csv.DictWriter(database, fieldnames=colm)
        writer.writerows(data)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        csv_file_writer(data)
        return render_template('thankyou.html', name=data['name'])

    else:
        print('Something went wrong. Try again....')


