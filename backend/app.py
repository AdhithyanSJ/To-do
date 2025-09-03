from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from backend.models import db, User
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash
from backend.controllers import signup, login, todoslist, todoitem

app = Flask(__name__)
api = Api(app)
CORS(app)
jwt = JWTManager(app)


app.config["JWT_SECRET_KEY"] = "open_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
        db.create_all()
        """if not User.query.filter_by(role='admin').first():
            admin = User(fullname='Adhi',
                         email='adhi@gmail.com',
                         password=generate_password_hash('open_admin'),
                         role='admin')
            db.session.add(admin)
            db.session.commit()"""



api.add_resource(signup, '/api/signup')
api.add_resource(login, '/api/login')
api.add_resource(todoslist, '/api/todoslist/<int:user_id>',endpoint='todoslist')
api.add_resource(todoitem, '/api/todoitem/<int:tid>',endpoint='todo')




if __name__ == '__main__':
    app.run(debug=True)