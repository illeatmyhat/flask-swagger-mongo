from datetime import datetime
from bson import ObjectId
from flask_admin.contrib.mongoengine import ModelView
from marshmallow_mongoengine import ModelSchema
from marshmallow.fields import Nested
from app.models.Person import Person, PersonSchema
from . import db, definitions


definitions['EventDate'] = {
    'type': 'object',
    'properties': {
        'type': {
            'type': 'string'
        },
        'start_date': {
            'type': 'string',
            'format': 'date-time'
        },
        'end_date': {
            'type': 'string',
            'format': 'date-time'
        }
    },
    'example': {
        'type': 'Birthday',
        'start_date': '2018-04-09T00:00:00+00:00',
        'end_date': '2018-04-08T23:59:59+00:00'
    }
}


class EventDate(db.EmbeddedDocument):
    type = db.StringField(max_length=100, required=True)
    start_date = db.DateTimeField(default=datetime.utcnow().date(), required=True)
    end_date = db.DateTimeField(default=datetime.utcnow().date())


definitions['Event'] = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'example': 'Surprise'
        },
        'dates': {
            'type': 'array',
            'items': {
                '$ref': '#/definitions/EventDate'
            }
        },
        'organizer': {
            '$ref': '#/definitions/Person'
        }
    }
}


class Event(db.Document):
    name = db.StringField(max_length=100, required=True)
    dates = db.ListField(db.EmbeddedDocumentField(EventDate))
    organizer = db.ReferenceField('Person')

    def __unicode__(self):
        return self.name

    # seems like you can't nest Schemas. Do it the old way.
    @staticmethod
    def serialize(event):
        result = event_schema.dump(event).data
        organizer = Person.objects.get(pk=event.to_mongo().get('organizer'))
        result['organizer'] = person_schema.dump(organizer).data
        return result

    @staticmethod
    def deserialize(event):
        organizer = Person.objects.get(pk=event['organizer'])
        event['organizer'] = person_schema.dump(organizer).data
        result = event_schema.load(event).data
        return result


class EventSchema(ModelSchema):
    class Meta:
        model = Event
    organizer = Nested('PersonSchema')


class EventView(ModelView):
    column_filters = ['name']
    column_list = ('name', 'dates', 'organizer')


event_schema = EventSchema()
person_schema = PersonSchema()
