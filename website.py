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
    MinecraftStatus = minecraft.status()
    MinecraftButtonText = "Start" if MinecraftStatus == "Inactive" else "Stop"
    if request.method == "POST":
        if MinecraftButtonText == "Start":
            minecraft.start()
            MinecraftStatus = minecraft.status()
        else:
            minecraft.stop()
            MinecraftStatus = minecraft.status()
    return render_template('minecraft.html', MinecraftButtonText=MinecraftButtonText, MinecraftStatus=MinecraftStatus)

if __name__ == '__main__':
    app.run(debug=True)