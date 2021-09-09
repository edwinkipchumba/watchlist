from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # Initializing flask extensions
    bootstrap.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setting config
    from .requests import configure_request
    configure_request(app)
    return app








# Initializing application
# app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# Initializing Flask Extensions
# bootstrap = Bootstrap(app)


# error import
# from app import views
# from app import error
