from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = '455a0595071af6e2385c0ec556cb329c'
db.init_app(app)
Migrate(app, db) #db init, db migrate, db upgrade, db downgrade
jwt = JWTManager(app)
CORS(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def users():
    if request.method == 'GET':
        users= User.query.all()
        users=list(map(lambda user: user.serialize_with_roles(),users))
        return jsonify(users), 200

if __name__ == '__main__':
    app.run()