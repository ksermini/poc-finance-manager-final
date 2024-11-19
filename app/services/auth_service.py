from app.models.user_model import User
from app.models.database import db

def authenticate_user(email, password):
    return User.query.filter_by(email=email, password=password).first()

def register_user(email, password):
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
