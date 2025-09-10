from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message" : "Learning GitHub Action"}), 200

@app.route('/githubactions')
def action():
    return jsonify({"message" : "Github Action Code running successfully"}), 200

@app.route('testprivaterepo')
def testPull():
    return jsonify({"message" : "Now EC2 could pull code from private repo"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)