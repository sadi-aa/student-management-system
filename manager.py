from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def create_student(self, name, age, student_id):
        s = Student(name, age, student_id)
        self.students.append(s)

    def view_students(self):
        for s in self.students:
            print(s.show_details())

    def update_student(self, student_id, name, age):
        for s in self.students:
            if s.student_id == student_id:
                s._Person__name = name
                s._Person__age = age
                break

    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]


