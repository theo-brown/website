from flask import Flask, render_template, redirect, request, jsonify
from os import getenv
from dotenv import load_dotenv
import hmac
import subprocess


load_dotenv()


app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/webhooks/website-update', methods=['POST'])
def website_repo_webhook():
    header_signature = request.headers.get('X-Hub-Signature-256')
    if not header_signature:
        return jsonify({'message': 'failure'}), 404

    sha_type, signature = header_signature.split('=')
    if sha_type != 'sha256':
        return  jsonify({'message': 'failure'}), 501

    hashed_secret = hmac.new(getenv('WEBSITE_UPDATE_WEBHOOK').encode(),
                             digestmod='sha256').hexdigest()

    if hmac.compare_digest(hashed_secret, signature):
        subprocess.run("./webhooks/website-update.sh")
        return jsonify({'message': 'success'}), 200
    else:
        return jsonify({'message': 'failure'}), 404


@app.route('/cv')
def cv_page():
    return redirect('https://raw.githubusercontent.com/theo-brown/cv/main/cv.pdf')


@app.route('/setup/python')
def setup_python_page():
    return redirect('https://raw.githubusercontent.com/theo-brown/setup/main/setup-python.sh')


if __name__ == '__main__':
    app.run(debug=True)