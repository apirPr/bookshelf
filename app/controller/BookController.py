from app import response, db
from app.model.User import Users
from app.model.Book import Books
from flask import request

def singleTransform(book):
  data = {
    'id': book.Books.id,
    'title': book.Books.title,
    'author': book.Books.author,
    'year': book.Books.year,
    'created_at': book.Books.created_at,
    'updated_at': book.Books.updated_at,
    'user_id': book.Books.user_id,
    'user': {
      'id': book.Users.id,
      'name': book.Users.name,
      'email': book.Users.email,
      'password': book.Users.password,
      'created_at': book.Users.created_at,
      'updated_at': book.Users.updated_at
    }
  }
  return data

def transform(books):
  array = []
  for i in books:
    array.append(singleTransform(i))
  return array

def get_all(request):
  try:
    books = db.session.query(Books, Users).join(Users).all()
    data = transform(books)
    return response.success(data, "success")
  except Exception as e:
    print(e)

def get(request, id):
  try:
    book = db.session.query(Books, Users).join(Users).filter(Books.id == id).first()
    if not book:
      return response.badRequest([], 'empty....')
    data = singleTransform(book)
    return response.success(data, "success")
  except Exception as e:
    print(e)

def create(request):
  try:
    title = request.json['title']
    author = request.json['author']
    year = request.json['year']
    user_id = request.json['user_id']

    book = Books(title=title, author=author, year=year, user_id=user_id)
    db.session.add(book)
    db.session.commit()

    return response.success('', 'success')
  except Exception as e:
    print(e)

def update(request, id):
  try:
    title = request.json['title']
    author = request.json['author']
    year = request.json['year']
    user_id = request.json['user_id']

    book = Books.query.filter_by(id=id).first()
    book.title = title
    book.author = author
    book.year = year
    book.user_id = user_id
    db.session.commit()

    return response.success('', 'success')
  except Exception as e:
    print(e)

def delete(request, id):
  try:
    book = Books.query.filter_by(id=id).first()
    if not book:
      return response.badRequest([], 'empty....')
    db.session.delete(book)
    db.session.commit()

    return response.success('', 'success')
  except Exception as e:
    print(e)

def search(request):
  try:
    title = request.args.get('title')
    books = db.session.query(Books, Users).join(Users).filter(Books.title.like('%'+title+'%')).all()
    if not books:
      return response.badRequest([], 'empty....')
    data = transform(books)
    return response.success(data, "success")
  except Exception as e:
    print(e)