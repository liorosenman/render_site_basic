from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="HEEEEEELO WORLD")

if __name__ == '__main__':
    app.run(debug=True)