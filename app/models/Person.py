from marshmallow_mongoengine import ModelSchema
from flask_admin.contrib.mongoengine import ModelView
from mongoengine.connection import get_db
from pymongo import TEXT
from slugify import slugify
from . import db, definitions

definitions['Person'] = {
    'type': 'object',
    'properties': {
        'first_name': {
            'type': 'string'
        },
        'last_name': {
            'type': 'string'
        },
        'email': {
            'type': 'string'
        },
        'slug': {
            'type': 'string'
        },
        'aliases': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        }
    },
    'example': {
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'John.Smith@usa.example.com',
        'slug': 'john-smith-usa-example-com',
        'aliases': ['Jimmy James', 'John M. Smith']
    }
}


class Person(db.Document):
    first_name = db.StringField(max_length=100, required=True)
    last_name = db.StringField(max_length=100, required=True)
    email = db.EmailField(max_length=100, required=True)
    slug = db.StringField(max_length=100)  # hidden field
    aliases = db.ListField(db.StringField(max_length=100))

    # not so easy to make a full text search index
    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        mongo = get_db()['Person']
        if '$**_text' not in mongo.index_information():
            mongo.create_index([('$**', TEXT)])

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)
        return super(Person, self).save(*args, **kwargs)

    @staticmethod
    def serialize(person):
        return person_schema.dump(person).data

    @staticmethod
    def deserialize(person):
        return person_schema.load(person).data


class PersonSchema(ModelSchema):
    class Meta:
        model = Person


class PersonView(ModelView):
    form_excluded_columns = {'slug'}

    column_filters = ['first_name']
    column_list = ('first_name', 'last_name', 'email', 'slug', 'aliases')


person_schema = PersonSchema()
