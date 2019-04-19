from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<men>')
def index(men):
    return render_template('index.html', var=men)

app.run(debug=True, host='0.0.0.0')
