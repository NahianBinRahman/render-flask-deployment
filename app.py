from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get-data')
def get_data():
    return jsonify({"message": "Hello from HTMX!"})


if __name__ == '__main__':
    app.run(debug=True)
