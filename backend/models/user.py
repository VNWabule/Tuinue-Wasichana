from datetime import datetime
from backend.config import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # donor, charity, admin
    is_active = db.Column(db.Boolean, default=True)

donations = db.relationship('Donation', backref='donor', lazy=True)
charity = db.relationship('Charity', backref='user', uselist=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)