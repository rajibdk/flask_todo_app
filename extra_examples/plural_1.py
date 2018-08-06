students = []
class Student:
    school_name = "Riju International School"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student {0} and Studied in {1}".format(self.name, self.get_school_name())
    
    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):
    def get_school_name(self):
        high_school_name = super().get_school_name() + " (High School)"
        return high_school_name

student = HighSchoolStudent("Neha")
print(student.get_school_name())