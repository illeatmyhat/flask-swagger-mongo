#!/usr/bin/env python3

import os

from flask import Flask
from app.models import *
from app.routes import event_blueprint, person_blueprint
from flask_admin import Admin
from flasgger import Swagger
from app.swagger import swagger_config, template


def main():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    swagger = Swagger(app, config=swagger_config, template=template)

    admin = Admin(app, 'Example: MongoEngine')
    admin.add_view(PersonView(Person, 'Person', endpoint='Person'))
    admin.add_view(EventView(Event, 'Event', endpoint='Event'))

    app.register_blueprint(event_blueprint, url_prefix='/api')
    app.register_blueprint(person_blueprint, url_prefix='/api')

    # Workaround for the werkzeug reloader removing the current directory from the
    # path. It's nasty, but it works! Inspired by:
    # https://github.com/mitsuhiko/flask/issues/1246
    os.environ['PYTHONPATH'] = os.getcwd()

    port = os.getenv('PORT', '8080')
    # app.run(port=int(port), ssl_context='adhoc)
    app.run(host='0.0.0.0', port=int(port))


if __name__ == '__main__':
    main()
