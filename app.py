from flask import Flask, render_template, request, redirect, url_for, flash
from modules.student_manager import StudentManager

app = Flask(__name__)
app.secret_key = '78589'  # Use a secure random key in production
manager = StudentManager()

# Home Page
@app.route('/')
def index():
    return render_template('index.html', students=manager.students)

# Add Student Page
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        surname = request.form['surname']
        try:
            manager.add_student(student_id, first_name, surname)
            flash('Student added successfully!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e), 'error')
    return render_template('add_student.html')

# Search Student Page
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

# Remove Student
@app.route('/remove/<student_id>', methods=['POST'])
def remove_student(student_id):
    try:
        manager.remove_student(student_id)
        flash('Student removed successfully!', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)