from app import response, db
from app.model.User import Users
from app.model.Book import Books
from flask import request


def single_transform(book):
    data = {
        "id": book.Books.id,
        "title": book.Books.title,
        "author": book.Books.author,
        "year": book.Books.year,
        "created_at": book.Books.created_at,
        "updated_at": book.Books.updated_at,
        "user_id": book.Books.user_id,
        "user": {
            "id": book.Users.id,
            "name": book.Users.name,
            "email": book.Users.email,
            "password": book.Users.password,
            "created_at": book.Users.created_at,
            "updated_at": book.Users.updated_at,
        },
    }
    return data


def transform(books):
    array = []
    for i in books:
        array.append(single_transform(i))
    return array


def get_all(request):
    try:
        books = db.session.query(Books, Users).join(Users).all()
        data = transform(books)
        return response.success(data, "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def get(request, id):
    try:
        book = db.session.query(Books, Users).join(Users).filter(Books.id == id).first()
        if not book:
            return response.not_found([], "Not Found")
        data = single_transform(book)
        return response.success(data, "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def create(request):
    try:
        title = request.json["title"]
        author = request.json["author"]
        year = request.json["year"]
        user_id = request.json["user_id"]
        finished = request.json["finished"]

        book = Books(
            title=title, author=author, year=year, user_id=user_id, finished=finished
        )
        db.session.add(book)
        db.session.commit()

        # creation success and send the book id
        return response.created(book.id, "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def update(request, id):
    try:
        title = request.json["title"]
        author = request.json["author"]
        year = request.json["year"]
        user_id = request.json["user_id"]

        book = Books.query.filter_by(id=id).first()
        book.title = title if title else book.title
        book.author = author if author else book.author
        book.year = year if year else book.year
        book.user_id = user_id if user_id else book.user_id
        db.session.commit()

        return response.success("", "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def delete(request, id):
    try:
        book = Books.query.filter_by(id=id).first()
        if not book:
            return response.not_found([], "Not Found")
        db.session.delete(book)
        db.session.commit()

        return response.success("", "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def search(request):
    try:
        title = request.args.get("title")
        books = (
            db.session.query(Books, Users)
            .join(Users)
            .filter(Books.title.like("%" + title + "%"))
            .all()
        )
        if not books:
            return response.not_found([], "Not Found")
        data = transform(books)
        return response.success(data, "success")
    except Exception as e:
        return response.internal_server_error([], str(e))


def finished(request, id):
    try:
        boolean = request.json["finished"]
        book = Books.query.filter_by(id=id).first()
        if not book:
            return response.not_found([], "Not Found")
        book.finished = boolean
        db.session.commit()

        return response.success(boolean, "success")

    except Exception as e:
        return response.internal_server_error([], str(e))
    
def search_by_title(request, title):
    try:
        books = (
            db.session.query(Books, Users)
            .join(Users)
            .filter(Books.title.like("%" + title + "%"))
            .all()
        )
        if not books:
            return response.not_found([], "Not Found")
        data = transform(books)
        return response.success(data, "success")
    except Exception as e:
        return response.internal_server_error([], str(e))
