from flask import Blueprint, jsonify

from api.errors import HTTPError

greeting_blueprint = Blueprint('greeting', __name__)


@greeting_blueprint.route('', methods=['GET'])
def base_greeting():
    '''Basic Blueprint.

    :returns: JSON Object, with basic greeting:

        +------------------------+--------------------------------------------+
        | Element                | Description                                |
        +========================+============================================+
        | - msg                  | Simple greeting from the api.              |
        +------------------------+--------------------------------------------+

    **Example request**:
        .. sourcecode:: http

            GET /api/greeting/ HTTP/1.1
            Host: 192.168.123.11
            Accept: application/json

    **Example response**:
        .. sourcecode:: http

            HTTP/1.0 200 OK
            Content-Type: application/json
            Content-Length: 44

            {
              "msg": "Hello World"
            }
    '''
    greeting_details = {
        'msg': "Hello World"
    }

    return jsonify(greeting_details)


@greeting_blueprint.route('/for', methods=['GET'])
@greeting_blueprint.route('/for/<name>', methods=['GET'])
def greeting(name=None):
    '''Basic Blueprint.

    :param name: Who to greet.
    :returns: JSON Object, containing greeting:

        +------------------------+--------------------------------------------+
        | Element                | Description                                |
        +========================+============================================+
        | - msg                  | Simple greeting message for a user.        |
        +------------------------+--------------------------------------------+

    **Example request**:
        .. sourcecode:: http

            GET /api/greeting/for/Kyle HTTP/1.1
            Host: 192.168.123.11
            Accept: application/json

    **Example response**:
        .. sourcecode:: http

            HTTP/1.0 200 OK
            Content-Type: application/json
            Content-Length: 21

            {
              "msg": "Hello Kyle"
            }
    '''
    if name is None:
        raise HTTPError("No one to greet", 400)

    greeting_details = {
        'msg': "Hello {}".format(name)
    }

    return jsonify(greeting_details)
