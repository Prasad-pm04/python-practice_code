class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, subject)

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Subject: {self.subject}")


ta = TeachingAssistant("Riya", 22, "S123", "Math")
ta.show_details()
