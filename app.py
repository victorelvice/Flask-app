from flask import Flask, render_template
import flask
app = Flask(__name__)

# Index
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)