from app import db
from app.model.User import Users
from app.model.Book import Books
from flask import session, url_for, redirect, render_template

def index(request):
  if 'user_id' in session:
    return redirect(url_for('dashboard'))
  return render_template('login.html')

def login(request):
  try:
    if 'user_id' in session:
      return redirect(url_for('dashboard'))
    
    email = request.json['email']
    password = request.json['password']
    user = Users.query.filter_by(email=email).first()

    if not user:
      return render_template('login.html', error='User tidak ditemukan')
    if not user.checkPassword(password):
      return render_template('login.html', error='Password salah', email=email)
    
    session['user_id'] = user.id
    session['user_name'] = user.name
    
    return redirect(url_for('dashboard'))
  except Exception as e:
    print(e)

def register(request):
  try:
    if 'user_id' in session:
      return redirect(url_for('dashboard'))

    user_already_exist = Users.query.filter_by(email=request.json['email']).first()

    if user_already_exist:
      return render_template('login.html', error='User sudah terdaftar')
    
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = Users(name=name, email=email)
    user.setPassword(password)
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id
    session['user_name'] = user.name

    return redirect(url_for('dashboard'))
  except Exception as e:
    print(e)

def logout(request):
  try:
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('login'))
  except Exception as e:
    print(e)

def dashboard(request):
  try:
    if 'user_id' not in session:
      return redirect(url_for('login'))
    return render_template('dashboard.html')
  except Exception as e:
    print(e)
