# Base class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")

# Derived class (Single Inheritance)
class Developer(Employee):
    def __init__(self, emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

# Further derived class (Multilevel Inheritance)
class TeamLead(Developer):
    def __init__(self, emp_id, name, salary, programming_language, team_size):
        super().__init__(emp_id, name, salary, programming_language)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

# Creating objects
e1 = Employee(101, "Rahul", 30000)
d1 = Developer(102, "Sneha", 50000, "Python")
t1 = TeamLead(103, "Arjun", 70000, "Java", 5)

# Displaying data
print("Employee Info:")
e1.display_details()

print("\nDeveloper Info:")
d1.display_details()

print("\nTeam Lead Info:")
t1.display_details()
