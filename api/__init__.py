import os
from flask import Flask, jsonify

from api.blueprints.example import greeting_blueprint
from errors import HTTPError
from utils import get_config


def register_server():
    app = Flask(__name__)

    settings_entry = os.environ.get('SKELETONS_SETTINGS_ENTRY', 'skeletons')
    server_settings = get_config(settings_entry)
    app.config['server_settings'] = server_settings

    app.config['SESSION_COOKIE_NAME'] = server_settings.cookie_name
    app.secret_key = server_settings.secret_key

    app.register_blueprint(greeting_blueprint, url_prefix='/greeting')

    @app.before_request
    def before_request():
        pass

    @app.teardown_request
    def teardown_request(error=None):
        pass

    @app.after_request
    def after_request(response):
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'error': 'Invalid API path'}), 404

    @app.errorhandler(HTTPError)
    def http_error(e):
        return jsonify({'error': e.msg}), e.status_code

    return app


def register_debug_server():
    from werkzeug.debug import DebuggedApplication
    app = register_server()
    app.debug = True
    app = DebuggedApplication(app, evalex=True)
    return app
