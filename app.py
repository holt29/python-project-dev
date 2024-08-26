from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    templateData = {}
    return render_template('homepage.html')


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
