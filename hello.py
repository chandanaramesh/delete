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
        arg = ['python2', 'client.py', '-ni', '-s', '2', '-c', 'show']
        proc1 = subprocess.Popen(['python3', 'groupjson.py'], stdout=subprocess.PIPE)
        output = json.loads(proc1.communicate()[0])
        group = {}
        for key, value in output.items():
            print('{} {}'.format(key,value))
            group.update(value)
        print(group)
            #for i, j in value.items():
             #   print('Inside first for loop: %s' %j)
    else: 
        print('Fail')
    return render_template('test.html', data=output)

if __name__ == '__main__':
    app.run(debug = True)
