class Student:
    def __init__(self, name, status="Absent"):
        self.name = name
        self.status = status


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def mark_attendance(self, name, status):
        for student in self.students:
            if student.name == name:
                student.status = status
                return
        print(f"Error: student '{name}' not found in classroom.")

    def show_report(self):
        for student in self.students:
            print(f"{student.name}: {student.status}")


classroom = Classroom()
classroom.add_student("Ali")
classroom.add_student("Sara")
classroom.add_student("Bilal")
classroom.add_student("Hina")

classroom.mark_attendance("Ali", "Present")
classroom.mark_attendance("Sara", "Present")
classroom.mark_attendance("NotAStudent", "Present")

classroom.show_report()
