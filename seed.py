
from app import app
from models import User, db

with app.app_context():
    print("Seeding user data..........")
    db.session.add(User(username="Felix", age=22))
    db.session.add(User(username="Brenda", age=19))
    db.session.add(User(username="Brighton", age=18))
    db.session.add(User(username="Ivy", age=20))
    db.session.add(User(username="Chelsea", age=30))
    
    db.session.commit()
    
    print("Done seeding")
    
    # db.session.add_all(list)
    # db.session.commit()