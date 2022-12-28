
from flask import request , jsonify, make_response
from flask import Flask
import os

from modules.rest import health as rest_health
from modules.rest import notebook as rest_notebook
from modules.rest import tag as rest_tag

import config

APP = Flask(__name__,static_folder='public', static_url_path='')

config.init()

EVERNOTE_BACKEND_CORS = os.environ.get("EVERNOTE_BACKEND_CORS")
if (EVERNOTE_BACKEND_CORS == 'true'):
   from flask_cors import CORS
   CORS(APP)



config.LOGGER.info("STARTUP EVERNOTE SERVICE")

@APP.route('/')
def index_html():
    config.LOGGER.info("GET / - received")
    config.LOGGER.info("GET / - result: OK")
    return config.APP.send_static_file('index.html')

@APP.route('/health')
def health():
    config.LOGGER.info("GET /health - received")
    result = rest_health.health(request)
    config.LOGGER.info("GET /health - result: {}".format(result['result']))
    resp = make_response(jsonify(result))
    #resp.headers['Test'] = 'my own header'
    return resp


@APP.route('/notebooks')
def notebooks():
    config.LOGGER.info(f'GET /notebooks - received')
    result = rest_notebook.get_notebooks(request)
    config.LOGGER.info("GET /notebooks - result: {}".format(result['result']))
    response = jsonify(result)
    return response

@APP.route('/tags')
def tags():
    config.LOGGER.info(f'GET /tags - received')
    result = rest_tag.get_tags(request)
    config.LOGGER.info("GET /tags - result: {}".format(result['result']))
    response = jsonify(result)
    return response


@APP.route('/notes')
def notes():
    notebook_guid = request.args.get('notebook_guid')
    config.LOGGER.info(f'GET /notes - received - notebook_guid: {notebook_guid}')
    result = rest_notebook.get_notes(request, notebook_guid)
    config.LOGGER.info("GET /notes - result: {}".format(result['result']))
    response = jsonify(result)
    return response


if __name__ == "__main__":
    #from waitress import serve
    #config.LOGGER.info("STARTUP waitress server on port %s ..." % (config.EVERNOTE_PORT))
    #serve(config.APP, host="0.0.0.0", port=config.EVERNOTE_PORT, threads=50)
    config.APP.run(host='0.0.0.0', port=config.EVERNOTE_PORT)


