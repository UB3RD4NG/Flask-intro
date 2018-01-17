from flask import Flask
from config import Config

site = Flask(__name__)
site.config.from_object(Config)

from app import routes
