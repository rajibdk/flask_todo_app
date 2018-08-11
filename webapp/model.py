from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "tbl_todo"
    todo_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(80), nullable=False)

    def __init__(self, todo_id, title, details):
        self.todo_id = todo_id
        self.title = title
        self.details = details

    def add_todo(_id, _title, _details):
        new_todo = Todo(todo_id=_id, title=_title, details=_details)
        db.session.add(new_todo)
        db.session.commit()
    
    def get_all_todos():
        return Todo.query.all()

    def find_todo_by_id(_id):
        return Todo.query.filter_by(todo_id=_id).first()
    
    def delete_todo_by_id(_id):
        Todo.query.filter_by(todo_id=_id).delete()
        db.session.commit()

    def update_todo(_id, _title, _details):
        todo = Todo.query.filter_by(todo_id=_id).first()
        todo.title = _title
        todo.details = _details
        db.session.commit()