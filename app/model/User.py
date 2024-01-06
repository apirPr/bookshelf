from app import db
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  email = db.Column(db.String(255), nullable=False, unique=True)
  name = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

  def __repr__(self):
    return '<User {}>'.format(self.name)
  
  def setPassword(self, password):
    self.password = generate_password_hash(password)

  def checkPassword(self, password):
    return check_password_hash(self.password, password)