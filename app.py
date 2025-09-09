from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message" : "Learning GitHub Action"})

@app.route('/githubactions')
def action():
    return jsonify({"message" : "Github Action Code running successfully"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)