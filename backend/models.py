from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    todo_list = db.relationship('todo', backref='User', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email,
            'role': self.role
        }
class todo(db.Model):
    tid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    status = db.Column(db.string(100),nullable=False,default="pending")
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    finished_at = db.Column(db.DateTime,nullable=True,default= None)