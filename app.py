from flask import Flask, json, render_template,jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/event1')
def event1():
    return jsonify(status="ok",application="College Tech Event",event="Event 1-2 hour hackathon")
@app.route('/event2')
def event2():
    return jsonify(status="ok",application="College Tech Event",event="Event 2-1 hour workshop")

@app.route('/event3')
def event3():
    return jsonify(status="ok",application="College Tech Event",event="Event 3-3 hour coding competition")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)