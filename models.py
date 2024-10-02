from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    age = db.Column(db.Integer)
    
    profile = db.relationship("Profile", backref="user", uselist=False, cascade="all, delete-orphan")
    
    posts = db.relationship("Post", back_populates="user")
    
class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
class Post(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    user = db.relationship("User", back_populates="posts")