
from app import app
from models import User, db, Profile

with app.app_context():
    # User.query.delete()
    db.session.query(User).delete()
    db.session.query(Profile).delete()
    db.session.commit()
    
    print("Seeding user data..........")
    
    # adding users
    user1 = db.session.add(User(username="Felix", age=22))
    user2 = db.session.add(User(username="Brenda", age=19))
    user3 = db.session.add(User(username="Brighton", age=18))
    user4 = db.session.add(User(username="Ivy", age=20))
    user5 = db.session.add(User(username="Chelsea", age=30))
    
    # Adding profiles
    profile1 = db.session.add(Profile(bio=" Lovely"))
    profile2 = db.session.add(Profile(bio="Caring" ))
    profile3 = db.session.add(Profile(bio="Love dancing"))
    
    
    # giving user profile
    # profile1.user_id = user1
    # profile2.user_id = user2
    # profile3.user_id = user3
    
    db.session.commit()

    
    print("Done seeding")
    
    # db.session.add_all(list)
    # db.session.commit()