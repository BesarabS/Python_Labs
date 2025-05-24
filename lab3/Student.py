class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Середній бал: {self.average_grade():.2f}"

    def grades_greater_than(self, number):
        return [grade for grade in self.grades if grade > number]


student = Student("Олена", 20, [85,92,78,88,90])
print(student)
print("Оцінки вище 85:", student.grades_greater_than(85))

student = Student("Станіслав", 21, [90,95,70,75,85])
print(student)
print("Оцінки вище 90:", student.grades_greater_than(90))

student = Student("Андрій", 19, [90,80,85,100,70])
print(student)
print("Оцінки вище 70:", student.grades_greater_than(70))