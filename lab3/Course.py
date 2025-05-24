from GraduateStudent import GraduateStudent
from Student import Student


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Можна додавати лише об'єкти класу Student або GraduateStudent.")

    def course_average(self):
        if not self.students:
            return 0
        total = sum(student.average_grade() for student in self.students)
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.average_grade())


student1 = Student("Олена", 20, [85,92,78,88,90])
student2 = GraduateStudent("Станіслав", 21, [90,95,70,75,85], "Створення додатку для IOS")

course = Course("Комп'ютерні науки")
course.add_student(student1)
course.add_student(student2)

print(f"Середній бал курсу: {course.course_average():.2f}")
print("Найкращий студент:", course.top_student())
