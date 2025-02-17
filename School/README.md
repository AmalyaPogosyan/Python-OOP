# School Management System

## 📌 Overview
This project simulates a **School Management System**, where teachers can assign grades, communicate with students, and students can submit assignments and track their grades. Classrooms manage students, teachers, and subjects efficiently.

## 🏗️ Features
- **Student Management**: Add, remove, and list students.
- **Teacher Management**: Assign teachers to classrooms.
- **Subject Management**: Assign subjects to teachers and classrooms.
- **Assignments & Grading**: Students submit assignments, and teachers grade them.
- **Messaging System**: Teachers can send messages to students.
- **Logging**: Actions are logged in a file.
- **Validation**: Ensures valid inputs using descriptors and custom exceptions.

## 📂 Project Structure
```
SchoolManagementSystem/
│── main.py                 # Main script
│── log.txt                 # Log file for tracking actions
│── README.md               # Project documentation
```

## 🔧 Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo-url.git
   ```
2. **Navigate to the project directory**:
   ```sh
   cd SchoolManagementSystem
   ```
3. **Run the script**:
   ```sh
   python main.py
   ```

## 🚀 Usage
### 1️⃣ Creating a Teacher & Student
```python
from main import Teacher, Student

t1 = Teacher("Amalya", 25, "amalya@mail.com")
s1 = Student("Arame", 15, "arame@mail.com")
```

### 2️⃣ Creating a Classroom & Assigning a Teacher
```python
from main import Classroom

c1 = Classroom("8A")
c1.assign_teacher(t1)
```

### 3️⃣ Adding a Student to a Classroom
```python
c1.add_student(s1)
```

### 4️⃣ Creating and Assigning a Subject
```python
from main import Subject

sub1 = Subject("Math", t1)
c1.add_subject(sub1)
```

### 5️⃣ Sending a Message from Teacher to Student
```python
t1.send_msj(s1, "Please submit your assignment.")
```

### 6️⃣ Student Submitting an Assignment
```python
s1.submit_assignment(t1, "Math", "My Homework")
```

### 7️⃣ Viewing Student Grades & Average Grade
```python
print(f"Grades for {s1.name}: {s1.grades}")
print(f"Average grade: {s1.average_grade()}")
```

## ⚠️ Error Handling
- **InvalidAgeError** → Raised when an invalid age is entered.
- **InvalidContactError** → Raised for incorrect email format.
- **PermissionError** → Raised when unauthorized actions are performed.

## 📝 License
This project is licensed under the **MIT License**.

---
### 💡 Author
Developed by **[Amalya Poghosyan]** 🚀

