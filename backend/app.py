from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from models import db, User
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash
from controllers import signup, login

app = Flask(__name__)
api = Api(app)
CORS(app)
jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
        db.create_all()
        if not User.query.filter_by(role='admin').first():
            admin = User(fullname='Adhi',
                         email='adhi@gmail.com',
                         password=generate_password_hash('open_admin'),
                         role='admin')
            db.session.add(admin)
            db.session.commit()

app.config["JWT_SECRET_KEY"] = "open_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///jsparking.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api.add_resource(signup, '/api/signup')
api.add_resource(login, '/api/login')



if __name__ == '__main__':
    app.run(debug=True)