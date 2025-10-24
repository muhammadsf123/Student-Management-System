from modules.student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade):
        student = Student(student_id, name, age, grade)
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students to display.")
        for student in self.students:
            print(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student removed successfully!")
                return
        print("Student not found.")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student found: ", student)
                return
        print("Student not found.")