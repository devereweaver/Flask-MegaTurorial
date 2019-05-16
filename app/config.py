import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Create a class that for the Secret Key configuration. As the application needs more configuration items, they can be added to this class.
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # The Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')   # Set configuration from envrionment variables, but provide a fallback 
    # Set to False to disable a feature of Flask-SQLAlchemy that we don't need. This feature signals the application everytime a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False 