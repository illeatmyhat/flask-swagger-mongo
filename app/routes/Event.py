from flask import Blueprint, request, jsonify
from app.models.Event import Event

event_blueprint = Blueprint("Event Blueprint", __name__)


@event_blueprint.route('/events', methods=['GET'])
def get_events():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - event
    responses:
      200:
        description: Many Event items
        schema:
          type: array
          items:
            $ref: "#/definitions/Event"
    """
    results = [Event.serialize(event) for event in Event.objects]
    return jsonify(results)


@event_blueprint.route('/events', methods=['POST'])
def post_events():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - event
    parameters:
      - in: query
        name: name
        type: string
        required: true
        description: "The name of the Event"
      - in: query
        name: organizer
        type: string
        required: true
        description: "The ObjectId of the organizer for the Event"
      - in: body
        name: dates
        schema:
          type: array
          items:
            $ref: "#/definitions/EventDate"
        description: "The number of items to retrieve"
    responses:
      200:
        description: Many Event items
        schema:
          type: array
          items:
            $ref: "#/definitions/Event"
    """
    event = {
        'name': request.args.get('name'),
        'organizer': request.args.get('organizer'),
        'dates': request.get_json(silent=True)
    }
    document = Event.deserialize(event)
    document.save()
    return jsonify('magic')
