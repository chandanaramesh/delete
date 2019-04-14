from flask import Flask
from flask import request,render_template
import sys
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    print('Standard', file=sys.stderr)
    if request.method == "GET":
        print('Success')
        proc1 = subprocess.Popen(['python3', 'testjson.py'], stdout=subprocess.PIPE)
    else: 
        print('Fail')
    return render_template('index.html', data='Hello')

if __name__ == '__main__':
    app.run(debug = True)
