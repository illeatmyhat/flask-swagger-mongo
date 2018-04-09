from flask import Blueprint, request, jsonify
# from flasgger import validate
from app.models.Person import Person
person_blueprint = Blueprint("Person Blueprint", __name__)


@person_blueprint.route('/person', methods=['GET'])
# @swagger.validate('')
def get_person():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - person
    parameters:
      - in: query
        name: search
        type: string
        required: true
        description: "The search terms--will find matching names, emails, and aliases"
      - in: query
        name: offset
        type: integer
        default: "0"
        minimum: 0
        description: "The number of items to skip"
      - in: query
        name: count
        type: integer
        default: 1
        minimum: 1
        description: "The number of items to retrieve"
    responses:
      200:
        description: Many Person items
        schema:
          type: array
          items:
            $ref: "#/definitions/Person"
    """
    search = request.args.get('search')
    offset = int(request.args.get('offset') or 0)
    count = int(request.args.get('count') or 1)
    results = [Person.serialize(person) for person in Person.objects.skip(offset).limit(count).search_text(search)]
    return jsonify(results)


@person_blueprint.route('/person', methods=['POST'])
def post_events():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - person
    parameters:
      - in: query
        name: first_name
        type: string
        required: true
        description: "The first name of the Person"
      - in: query
        name: last_name
        type: string
        required: true
        description: "The last name of the Person"
      - in: query
        name: email
        type: string
        required: true
        description: "The email of the Person"
      - in: query
        name: aliases
        type: array
        items:
          type: string
        description: "Any aliases the person may have"
    responses:
      200:
        description: Many Event items
        schema:
          type: array
          items:
            $ref: "#/definitions/Event"
    """
    person = {
        'first_name': request.args.get('first_name'),
        'last_name': request.args.get('last_name'),
        'email': request.args.get('email'),
        'aliases': request.args.get('aliases').split(',')
    }
    document = Person.deserialize(person)
    document.save()
    return 'magic'
