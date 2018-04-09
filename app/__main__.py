#!/usr/bin/env python3

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

    # app.run(port=8080, ssl_context='adhoc')
    app.run(port=8080)


if __name__ == '__main__':
    main()
