from flask_restful import Resource
from flask import request,jsonify
from backend.models import User, db , Todo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

class login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            return {"message": "User doesnt exist"}, 400
        if not check_password_hash(user.password,password):
            return {"message": "Invalid password"}, 401
        token = create_access_token(identity=email)

        return {
            "message": "Login successful",
            "user": user.to_dict(),
            "token": token
        }, 200
    
class signup(Resource):
    def post(self):
        data = request.get_json()
        fullname = data.get('fullname')
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            return {"message": "User already exists"}, 400
        new_user = User(
            fullname=fullname,
            email=email,
            password=generate_password_hash(password),
            role='user'
        )
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully please login"}, 201
    
class todoslist(Resource):
    @jwt_required()
    def get(self,user_id):
        current_user_email = get_jwt_identity()
        user = User.query.filter_by(email=current_user_email).first()
        if not user:
            return {"message": "User not found"}, 404
        todos = [todo_item.to_dict() for todo_item in user.todo_list]
        return todos, 200
    @jwt_required()
    def post(self,user_id):
        data = request.get_json()
        name = data.get('name')
        status = data.get('status', 'pending')
        new_todo = Todo(
            name=name,
            status=status,
            user_id=user_id
        )
        db.session.add(new_todo)
        db.session.commit()
        return {"message": "Todo created successfully", "todo": new_todo.to_dict()}, 200
class todoitem(Resource):
    @jwt_required()
    def put(self, tid):
        data = request.get_json()
        todo_item = Todo.query.get(tid)
        status = data.get('status')
        if (status=="completed"):
            todo_item.status = status
            db.session.commit()
            return {"message": "Task finished"}, 200
    @jwt_required()
    def delete(self, tid):
        todo_item = Todo.query.get(tid)
        db.session.delete(todo_item)
        db.session.commit()
        return {"message": "Task deleted"}, 200