from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, User, Post, Profile
from flask_cors import CORS

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
CORS(app)
# Bulding APIs
# http => GET, POST, PATCH OR DELETE
# GET => Retrieve all the records from the database
#     => retrieve a single record from the database
    
# POST => Creating a new record and inserting it into the database

# PATCH => Update some record fields

# DELETE => Removes records from the database

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        # GET => Retrieve all the records from the database  
        posts =  [post.to_dict() for post in Post.query.all()]
        # print(posts)
        return make_response(posts, 200)
    
    if request.method == 'POST':
        # POST => Creating a new record and inserting it into the database
        data = request.get_json()
        
        # create post instance then save it to the database
        new_post = Post(content=data['content'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()
        
        return make_response({"message": "Post created successfully"})

@app.route('/posts/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def post(id):
    post = Post.query.get(id)
    if not post:
        return make_response({"message": "No post found"}, 404)
    
    if request.method == 'GET':
        
        return make_response(post.to_dict(), 200)
    
    if request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        
        return make_response({"message": "post deleted"}, 200)
    
    if request.method == 'PATCH':
        pass
    
# => retrieve a single record from the database

# PATCH => Update some record fields
# DELETE => Removes records from the database

if __name__ == '__main__':
    app.run(port=5500, debug=True)