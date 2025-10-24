class Student:
    def __init__(self, student_id, first_name, surname, grade):
        self.student_id = student_id
        self.first_name = first_name
        self.surname = surname
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, First Name: {self.first_name}, Surname: {self.surname}, Grade: {self.grade}"
