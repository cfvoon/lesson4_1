from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        num_A = request.form['A']
        num_B = request.form['B']
        final_result = num_A + num_B
        return render_template('index.html', href2='A + B = '+str(final_result))
