import json
import os
from modules.student import Student

class StudentManager:
    def __init__(self, data_file="data/students.json"):
        self.data_file = data_file
        self.students = []
        self.load_students()

    # ✅ Load existing students from JSON
    def load_students(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self.students = [Student(**student) for student in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading students: {e}. Starting with empty list.")
                self.students = []
        else:
            self.students = []

    # ✅ Save students to JSON
    def save_students(self):
        try:
            with open(self.data_file, "w") as file:
                json.dump([student.__dict__ for student in self.students], file, indent=4)
        except IOError as e:
            raise ValueError(f"Failed to save students: {e}")

    def add_student(self, student_id, first_name, surname):
        if not student_id or not first_name or not surname:
            raise ValueError("All fields (student_id, first_name, surname) are required.")
        if any(s.student_id == student_id for s in self.students):
            raise ValueError(f"Student with ID {student_id} already exists.")
        student = Student(student_id, first_name, surname)
        self.students.append(student)
        self.save_students()
        print("Student added and saved successfully!")

    def display_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students:
                print(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student removed and saved successfully!")
                return
        raise ValueError(f"Student with ID {student_id} not found.")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student found:", student)
                return
        print("Student not found.")