from flask import Flask, render_template, json, jsonify, request
import minecraft

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match_config')
def match_config_page():
    with open("/home/theo/Documents/projects/discord/matchbot/get5/configs/match_config.json") as f:
        config = json.load(f)
    return jsonify(config)

@app.route('/minecraft', methods=["POST", "GET"])
def minecraft_page():
    MinecraftStatusText = minecraft.status_text()
    MinecraftButtonText = "Stop" if minecraft.is_running() else "Start"

    if request.method == "POST":
        if MinecraftButtonText == "Start":
            minecraft.start()
            MinecraftStatusText = minecraft.status_text()
            MinecraftButtonText = "Stop"
        else:
            minecraft.stop()
            MinecraftStatusText = minecraft.status_text()
            MinecraftButtonText = "Start"
    return render_template('minecraft.html', MinecraftButtonText=MinecraftButtonText, MinecraftStatusText=MinecraftStatusText)

if __name__ == '__main__':
    app.run(debug=True)