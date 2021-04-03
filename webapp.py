from flask import Flask, render_template, json, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match_config')
def match_config():
    with open("/home/theo/Documents/projects/discord/matchbot/get5/configs/match_config.json") as f:
        config = json.load(f)
    return jsonify(config)

MinecraftButtonText = "Start"
@app.route('/minecraft', methods=["POST", "GET"])
def minecraft():
    global MinecraftButtonText
    if request.method == "POST":
        if MinecraftButtonText == "Start":
            MinecraftButtonText = "Stop"
        else:
            MinecraftButtonText = "Start"
    return render_template('minecraft.html', MinecraftButtonText=MinecraftButtonText)

if __name__ == '__main__':
    app.run(debug=True)