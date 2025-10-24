from flask import Flask, render_template, request, redirect, url_for, flash
from modules.student_manager import StudentManager

app = Flask(__name__)
app.secret_key = '78589'  # Change this to a random secret key
manager = StudentManager()

@app.route('/')
def index():
    return render_template('index.html', students=manager.students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        surname = request.form['surname']
        grade = request.form['grade']
        manager.add_student(student_id, first_name, surname, grade)
        flash('Student added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    student = None
    if request.method == 'POST':
        student_id = request.form['student_id']
        for s in manager.students:
            if s.student_id == student_id:
                student = s
                break
        if not student:
            flash('Student not found.', 'error')
    return render_template('search_student.html', student=student)

@app.route('/remove/<student_id>', methods=['POST'])
def remove_student(student_id):
    manager.remove_student(student_id)
    flash('Student removed successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
