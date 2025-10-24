from flask import Flask, render_template, request, redirect
from modules.student_manager import StudentManager

app = Flask(__name__)
manager = StudentManager("data/students.json")

# Home Page Route
@app.route("/")
def index():
    return render_template("index.html", students=manager.students)

# Route to Add Student (Form submits here)
@app.route("/add_student", methods=["POST"])
def add_student():
    student_id = request.form["student_id"]
    name = request.form["name"]
    age = request.form["age"]
    grade = request.form["grade"]
    manager.add_student(student_id, name, age, grade)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)