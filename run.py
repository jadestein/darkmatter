from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('Baby Girl')

@app.route('/adam')
def adam():
    return('Call me at (305) 965-9445')

@app.route('/steven')
def steven():
    return('I love Adam because he is the best son ever. Adam will go to MIT.')

@app.route('/<number>')
def hello(number):
    return('Hello. That is a great lucky number. My favorite is also #' + number)

app.run(debug=True, host='0.0.0.0')