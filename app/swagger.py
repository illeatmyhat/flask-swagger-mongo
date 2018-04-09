from app.models import definitions

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'swagger',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/ui",
    "title": "Party API",
    "uiversion": 2
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "Party API",
        "description": "API for my party",
        "contact": {
            "name": "John Doe",
            "email": "spam@example.com",
            "url": "www.example.com",
        },
        "termsOfService": "http://example.com/terms",
        "version": "0.0.1"
    },
    # "basePath": "/api",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "definitions": definitions
}