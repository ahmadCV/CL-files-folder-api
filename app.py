import os.path

import flask
from flask import request
from flask_cors import CORS

from natsort import natsorted

app = flask.Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/send', methods=['POST'])
def get_data():
    f = request.files['file']
    folder_name = request.form['folder']

    if not os.path.isdir('data'):
        os.mkdir('data')

    if not os.path.isdir(f'data/{folder_name}'):
        os.mkdir(f'data/{folder_name}')
    f.save(f"data/{folder_name}/{f.filename}")
    f.flush()
    f.close()

    return 'operation successful'


@app.route('/get_latest', methods=['GET'])
def get_latest_folder_name():
    try:
        dirs = os.listdir('data')
        latest_dir = natsorted(dirs)[-1]

        return latest_dir
    except Exception as e:
        return 'ERROR: No data available'


if __name__ == '__main__':
    app.run()
