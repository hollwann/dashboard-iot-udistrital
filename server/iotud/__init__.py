import os
from flask import Flask
from flask_cors import CORS


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="ASDOIVNEOVNOSDV",
    )
    # apply the blueprints to the app
    from iotud.api import users

    app.register_blueprint(users.bp)

    CORS(app, resources={r"/*": {"origins": "*"}})
    return app
