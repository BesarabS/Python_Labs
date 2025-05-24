from Student import Student

class GraduateStudent(Student):
    def __init__(self, name, age, grades, thesis_topic):
        super().__init__(name, age, grades)
        self.thesis_topic = thesis_topic

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Тема дипломної роботи: {self.thesis_topic}"


grad_student = GraduateStudent("Олена", 20, [85,92,78,88,90], "Штучний інтелект у медицині")
print(grad_student)

grad_student = GraduateStudent("Станіслав", 21, [90,95,70,75,85], "Створення додатку для IOS")
print(grad_student)