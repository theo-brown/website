from flask import Flask, render_template, redirect


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


if __name__ == '__main__':
    app.run(debug=True)