from flask import Flask, redirect, render_template, request, session, url_for
import os
import secrets

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")


@app.get("/")
def index():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(24)
    return render_template("index.html", tasks=session.get("tasks", []))


@app.post("/tasks")
def add_task():
    if request.form.get("csrf_token") != session.get("csrf_token"):
        return "잘못된 요청입니다.", 400
    title = request.form.get("title", "").strip()[:100]
    tasks = session.get("tasks", [])
    if title and len(tasks) < 12:
        tasks.append({"id": secrets.token_hex(8), "title": title, "done": False})
        session["tasks"] = tasks
    return redirect(url_for("index", _anchor="planner"))


@app.post("/tasks/<task_id>/toggle")
def toggle_task(task_id):
    if request.form.get("csrf_token") != session.get("csrf_token"):
        return "잘못된 요청입니다.", 400
    tasks = session.get("tasks", [])
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    session["tasks"] = tasks
    return redirect(url_for("index", _anchor="planner"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
