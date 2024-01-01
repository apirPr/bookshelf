from app import app
from app.controller import UserController, BookController
from flask import request

# login route
@app.route('/', methods=['GET'])
def index():
  return 'Hello World'