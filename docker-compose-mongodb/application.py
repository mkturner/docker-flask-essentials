from flask import Flask
from flask_mongoengine import MongoEngine


# Instantiate instance of class
db = MongoEngine()

# Create Factory w/ config overrides
def create_app(**config_overrides):
    # Instantiate Flask object
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply test overrides
    app.config.update(config_overrides)

    # Initialize db
    db.init_app(app)

    # Import blueprints
    from counter.views import counter_app

    # Register blueprints
    app.register_blueprint(counter_app)
 
    return app