# _*_ coding: utf-8 _*_
# Author: Maksim.G

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_object("config")

db = MongoEngine(app)

from app import views, models



