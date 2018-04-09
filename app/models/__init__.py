from flask_mongoengine import MongoEngine
db = MongoEngine()
definitions = {}

from app.models.Person import Person, PersonSchema, PersonView
from app.models.Event import Event, EventSchema, EventView
