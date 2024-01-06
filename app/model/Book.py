from app import db
from datetime import datetime 
from app.model.User import Users

class Books(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  title = db.Column(db.String(255), nullable=False)
  author = db.Column(db.String(255), nullable=False)
  year = db.Column(db.String(255), nullable=False)
  finished = db.Column(db.Boolean, nullable=False, default=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id), nullable=False)
  user = db.relationship(Users, backref=db.backref('user_id', lazy=True))

  def __repr__(self):
    return '<Todo {}>'.format(self.title)