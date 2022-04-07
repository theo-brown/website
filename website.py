from flask import Flask, render_template, redirect, request, send_file, jsonify
from os import getenv
from dotenv import load_dotenv
import hmac
import subprocess


load_dotenv()


app = Flask(__name__)

# PAGES

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/cv')
def cv_page():
    return send_file('static/files/cv/cv.pdf')


@app.route('/setup/conda')
def setup_conda_page():
    return send_file('static/files/setup/conda-setup.sh')


@app.route('/setup/ssh')
def setup_ssh_page():
    return send_file('static/files/setup/ssh-setup.sh')


@app.route('/setup/docker')
def setup_docker_page():
    return send_file('static/files/setup/docker-setup.sh')


# WEBHOOKS
def verify_signature(request_object, signature, secret):
    hashed_secret = hmac.new(secret.encode(),
                             msg=request_object.get_data(),
                             digestmod='sha256').hexdigest()
    return hmac.compare_digest(hashed_secret, signature)


def verify_github_webhook(request_object, secret):
    header_signature = request_object.headers.get('X-Hub-Signature-256')
    if not header_signature:
        return False
    sha_type, signature = header_signature.split('=')
    return verify_signature(request_object, signature, secret)


def run_webhook(request, secret, commands):
   if verify_github_webhook(request, secret):
        process = subprocess.run(commands, cwd=getenv('WEBSITE_DIR'))
        if process.returncode == 0:
            return jsonify({'message': 'success'}), 200
        else:
            return jsonify({'message': 'failure'}), 500
    else:
        return jsonify({'message': 'failure'}), 404


@app.route('/webhooks/setup-update', methods=['POST'])
def setup_update_webhook():
    return run_webhook(request,
                       getenv('SETUP_UPDATE_WEBHOOK_SECRET'),
                       ["bash", "webhooks/setup-update.sh"])


@app.route('/webhooks/website-update', methods=['POST'])
def website_update_webhook():
    return run_webhook(request,
                       getenv('WEBSITE_UPDATE_WEBHOOK_SECRET'),
                       ["bash", "webhooks/setup-update.sh"])


@app.route('/webhooks/cv-update', methods=['POST'])
def cv_update_webhook():
    return run_webhook(request,
                       getenv('CV_UPDATE_WEBHOOK_SECRET'),
                       ["bash", "webhooks/cv-update.sh"])


if __name__ == '__main__':
    app.run(debug=True)
