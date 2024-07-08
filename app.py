from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="HEEEEEELO WORLD")

if __name__ == '__main__':
    app.run(debug=True)