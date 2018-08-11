from flask import Flask, request, render_template, url_for, redirect
from settings import app
from model import Todo
import os

port = int(os.getenv('PORT', '3000'))

@app.route("/", methods=["GET", "POST"])
def todos_page():
    if request.method == "POST":
        todo_id = request.form.get("todo_id", "")
        title = request.form.get("title", "")
        details = request.form.get("details", "")
        method = request.form.get("_method", "")

        if method == "PATCH":
            process_patch_request()
        else:
            Todo.add_todo(_id=todo_id, _title=title, _details=details)
        return redirect(url_for("todos_page"))
    
    todos = Todo.get_all_todos()
    return render_template("index.html", todos=todos)


def process_patch_request():
    todo_id = request.form.get("todo_id_edit", "")
    title = request.form.get("todo_title_edit", "")
    details = request.form.get("todo_details_edit", "")
    Todo.update_todo(_id=todo_id, _title=title, _details=details)


@app.route("/todo/<todo_id>", methods=["DELETE"])
def todos_delete(todo_id):
    Todo.delete_todo_by_id(_id=todo_id)
    todos = Todo.get_all_todos()
    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
