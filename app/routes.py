from app import app
from app.controller import UserController, BookController
from flask import request

# route index
@app.route('/', methods=['GET'])
def index():
  return UserController.index(request)

# login route for user
@app.route('/login', methods=['POST', 'GET'])
def login():
  return UserController.login(request)

# register route for user
@app.route('/register', methods=['POST', 'GET'])
def register():
  return UserController.register(request)

# route logout
@app.route('/logout', methods=['GET'])
def logout():
  return UserController.logout(request)

# route dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
  return UserController.dashboard(request)

# route get all books
@app.route('/books', methods=['GET'])
def books():
  return BookController.get_all(request)

# route get book by id
@app.route('/book/<id>', methods=['GET'])
def book(id):
  return BookController.get(request, id)

# route create book
@app.route('/book', methods=['POST'])
def create_book():
  return BookController.create(request)

# route update book
@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
  return BookController.update(request, id)

# route book finished
@app.route('/book/<id>', methods=['PATCH'])
def book_finished(id):
  return BookController.finished(request, id)

# route delete book
@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
  return BookController.delete(request, id)

# route search book
@app.route('/search', methods=['GET'])
def search():
  return BookController.search(request)

# route search by title
@app.route('/search/<title>', methods=['GET'])
def search_by_title(title):
  return BookController.search_by_title(request, title)