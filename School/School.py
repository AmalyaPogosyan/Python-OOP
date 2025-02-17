from abc import ABC, abstractmethod
from datetime import datetime
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Custom exceptions
class InvalidAgeError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class InvalidContactError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class PermissionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

# Attribute validation using descriptors
class Validator:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"'{self.name}' must be of type '{self.expected_type.__name__}'.")

        if isinstance(value, str) and not value.strip():
            raise ValueError(f"'{self.name}' cannot be an empty string.")

        if isinstance(value, int) and value < 0:
            raise InvalidAgeError(f"'{self.name}' must be a positive integer.")

        if self.name == 'email' and not is_valid_email(value):
            raise InvalidContactError('Invalid email format.')
        
        instance.__dict__[self.name] = value

# Logging decorator
def log_action(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        with open('log.txt', 'a') as log_file:
            log_file.write(f"[{datetime.now()}] '{fn.__name__}' called with {', '.join(repr(arg) for arg in args[1:])}\n")
        return result
    return wrapper

# Abstract base class for people
class Person(ABC):
    name = Validator(str)
    age = Validator(int)
    email = Validator(str)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @abstractmethod
    def get_details(self):
        pass

# Teacher class
class Teacher(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age, email)
        self.subjects = []

    def grade_assignments(self, student, subject, assignment):
        if subject not in student.grades:
            student.grades[subject] = []
        student.grades[subject].append(len(assignment))

    def send_msj(self, student, msg):
        if self not in student.msjs:
            student.msjs[self] = []
        student.msjs[self].append(msg)

    def get_details(self):
        return f"Teacher | Name: {self.name} | Age: {self.age} | Email: {self.email}"
    
    def __repr__(self):
        return self.name

# Student class
class Student(Person):
    def __init__(self, name, age, email):
        super().__init__(name, age, email)
        self.grades = {}
        self.msjs = {}  # teacher: messages

    def submit_assignment(self, teacher, subject, assignment):
        teacher.grade_assignments(self, subject, assignment)

    def average_grade(self):
        total_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades]
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __repr__(self):
        return self.name
    
    def get_details(self):
        return f"Student | Name: {self.name} | Age: {self.age} | Email: {self.email}"

# Subject class
class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def get_subject_info(self):
        return f"Subject: '{self.name}' | Teacher: {self.teacher}"
    
    def __repr__(self):
        return self.name

# Classroom class
class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []
        self.teacher = None  # Added teacher attribute

    @log_action
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('Expected a Student object.')
        self.students.append(student)
    
    @log_action
    def add_subject(self, subject):
        if not isinstance(subject, Subject):
            raise TypeError('Expected a Subject object.')
        self.subjects.append(subject)

    def remove_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('Expected a Student object.')
        if student not in self.students:
            raise ValueError(f'Student {student.name} is not in this classroom.')
        self.students.remove(student)

    def list_students(self):
        if not self.students:
            return "Empty classroom"
        return [student.get_details() for student in self.students]

    @log_action
    def assign_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError('Expected a Teacher object.')
        self.teacher = teacher

# Testing the functionality
t1 = Teacher('Amalya', 25, 'amal@mail.ru')
s1 = Student('Arame', 15, 'aram@mail.ru')
sub1 = Subject('Math', t1)
c1 = Classroom('8A')

c1.assign_teacher(t1)
c1.add_student(s1)
c1.add_subject(sub1)

t1.send_msj(s1, "Please submit your assignment.")
t1.send_msj(s1, "Don't forget the deadline.")

s1.submit_assignment(t1, 'Math', "My Homework")

# Print results
print(f"Teacher: {t1.get_details()}")
print(f"Student: {s1.get_details()}")
print(f"Subjects: {[sub.get_subject_info() for sub in c1.subjects]}")
print(f"Classroom Students: {c1.list_students()}")
print(f"Messages for {s1.name}: {s1.msjs}")
print(f"Grades for {s1.name}: {s1.grades}")
print(f"Average grade for {s1.name}: {s1.average_grade()}")
