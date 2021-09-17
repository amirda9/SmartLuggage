from flask import Response
from flask import Flask
from flask import render_template
from flask import jsonify
import threading
import datetime
import time
import random

output = 0
lock = threading.Lock()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/live_signal')
def live_signal():
    global output, lock
    with lock:
        #print('aaa',output)
        return jsonify(final_signal = output)

def gen():
    random_number = random.randint(1, 100)
    time.sleep(1)
   # print(random_number)
    return random_number

def run_signal():
    global output, lock
    while True:
        temp = gen()
        with lock:
            output = temp


if __name__ == '__main__':
    t = threading.Thread(target = run_signal)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True, use_reloader=False)

# vs.stop()
