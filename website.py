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


@app.route('/cv')
def cv_page():
    return redirect('https://raw.githubusercontent.com/theo-brown/cv/main/cv.pdf')


@app.route('/setup/python')
def setup_python_page():
    return redirect('https://raw.githubusercontent.com/theo-brown/setup/main/setup-python.sh')


@app.route('/webhooks/website-update', methods=['POST'])
def website_update_webhook():
    if verify_github_webhook(request, getenv('WEBSITE_UPDATE_WEBHOOK')):
        subprocess.run(["sh", f"{getenv('ROOT_DIR')}/webhooks/website-update.sh"])
        return jsonify({'message': 'success'}), 200
    else:
        return jsonify({'message': 'failure'}), 404


def verify_signature(request, signature, secret):
    hashed_secret = hmac.new(secret.encode(),
                             msg=request.get_data(),
                             digestmod='sha256').hexdigest()
    return hmac.compare_digest(hashed_secret, signature)


def verify_github_webhook(request, secret):
    header_signature = request.headers.get('X-Hub-Signature-256')
    if not header_signature:
        return False
    sha_type, signature = header_signature.split('=')
    return verify_signature(request, signature, secret)


if __name__ == '__main__':
    app.run(debug=True)
