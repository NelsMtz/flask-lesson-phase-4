from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, User

# create a Flask application object
app = Flask(__name__)

# configure a database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/users/<username>')
def getUsername(username):
    return f'Welcome to flask development {username}'

@app.route('/users')
def getUsers():
    users =[{"id": user.id, "username": user.username, "age": user.age } for user in User.query.all()]
    # print(users)
    return make_response(users, 200)

if __name__ == '__main__':
    app.run(port=5500, debug=True)