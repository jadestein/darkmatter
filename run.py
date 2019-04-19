from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('Baby Girl')

app.run(debug=True)