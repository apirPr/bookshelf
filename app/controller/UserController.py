from app import db, response
from app.model.User import Users
from app.model.Book import Books
from flask import session, url_for, redirect, render_template
from datetime import datetime


def index(request):
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

def single_transform(user):
    data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }
    return data

def login(request):
    try:
        if request.method == "GET":
            return render_template("login.html")

        if "user_id" in session:
            return redirect(url_for("dashboard"))

        email = request.json["email"]
        password = request.json["password"]
        user = Users.query.filter_by(email=email).first()

        if not user:
            return response.not_found([], "User tidak ditemukan")
        if not user.checkPassword(password):
            return response.unauthorized([], "Password salah")

        session["user_id"] = user.id
        session["user_name"] = user.name

        return response.success(single_transform(user), "Login berhasil")
    except Exception as e:
        print(e)
        return response.internal_server_error([], str(e))


def register(request):
    try:
        if request.method == "GET":
            return render_template("register.html")
        
        if "user_id" in session:
            return redirect(url_for("dashboard"))

        user_already_exist = Users.query.filter_by(email=request.json["email"]).first()

        if user_already_exist:
            return response.conflict([], "Email sudah terdaftar")

        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        user = Users(name=name, email=email, created_at=datetime.now(), updated_at=datetime.now())
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        session["user_name"] = user.name

        return response.created(single_transform(user), "Registrasi berhasil")
    except Exception as e:
        print(e)
        return response.internal_server_error([], str(e))


def logout(request):
    try:
        session.pop("user_id", None)
        session.pop("user_name", None)
        return response.success([], "Logout berhasil")
    except Exception as e:
        return response.internal_server_error([], str(e))


def dashboard(request):
    try:
        if "user_id" not in session or "user_name" not in session:
            return redirect(url_for("login"))
        return render_template("dashboard.html", user_id=session["user_id"], user_name=session["user_name"])
    except Exception as e:
        return response.internal_server_error([], str(e))
