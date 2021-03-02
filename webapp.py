from flask import Flask, render_template, json, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match_config')
def match_config():
    with open("/home/tab53/programs/matchbot/get5/configs/match_config.json") as f:
        config = json.load(f)
    return jsonify(config)
