from app import db
from datetime import datetime 
from app.model.User import Users

class Books(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  title = db.Column(db.String(255), nullable=False)
  author = db.Column(db.String(255), nullable=False)
  year = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return '<Todo {}>'.format(self.title)