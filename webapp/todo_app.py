from flask import Flask, request, render_template, url_for, redirect
from todo import Todo

app = Flask(__name__)
todos = []


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
            todo = Todo(todo_id, title, details)
            todos.append(todo)

        return redirect(url_for("todos_page"))

    return render_template("index.html", todos=todos)


def process_patch_request():
    todo_id = request.form.get("todo_id_edit", "")
    title = request.form.get("todo_title_edit", "")
    details = request.form.get("todo_details_edit", "")
    for todo in todos:
        if todo.todo_id == todo_id:
            todo.title = title
            todo.details = details


@app.route("/todo/<todo_id>", methods=["DELETE"])
def todos_delete(todo_id):
    i = 0
    for todo in todos:
        if todo.todo_id == todo_id:
            todos.pop(i)
            break
        i += 1
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
