# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
import requests

from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory
import json
import os

# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('config.BaseConfig')


@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('index.html')


@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''

    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_embed_params_for_single_report(app.config['WORKSPACE_ID'],
                                                                          report_id="29204b97-e9de-40e9-aed3-f3f54fd4297f")
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500


@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/reports', methods=['GET'])
def get_report_id_list():
    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    response = PbiEmbedService().get_report_ids_for_single_workspace(workspace_id=app.config['WORKSPACE_ID'])
    return response, 200


if __name__ == '__main__':
    app.run()
