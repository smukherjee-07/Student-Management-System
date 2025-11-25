# 🎓 Student Management System(SMS)

## 📌 Overview

The **Student Management System (SMS)** is a console-based Python application designed to store, manage, and update student records efficiently. It replaces manual record-keeping with persistent digital storage using **JSON**, while enforcing secure access through role-based authentication.

The system supports student enrollment, attendance logging, marks entry, and controlled administrative operations to ensure data integrity across sessions.

## 🏗 System Design

The program follows a modular structure allowing scalability and easy maintenance.

## Execution flow:
User Input → Validation → Processing → Permanent Storage (JSON)

### 🗂 Data Storage

The system uses two JSON files:

| File Name | Purpose |
|-----------|---------|
| `users.json` | Stores login credentials and role permissions |
| `students.json` | Contains personal information, subjects, marks, and attendance |

If these files are missing during the first run, they are automatically created by the system.

## 🧩 Core Functional Components

### 🔐 Authentication & Roles

- System ensures one admin exists — if not, it prompts one to be created.
- Access Levels:
  - **Admin:** Full permissions including adding, viewing, modifying, and deleting data.
  - **User:** Limited to view access and academic updates.

### 🎓 Student Management Features

- **Enroll Student:** Adds new student details with validation and prevents duplicate registration numbers.
- **View Student Records:** Displays all stored students or fetches a specific record via registration number lookup.
- **Delete Student:** Admin-only action allowing secure record removal.

### 📚 Academic Operations

- **Add Marks:** Records subject-wise marks with input validation.
- **Mark Attendance:** Logs attendance with timestamps automatically.

## 🚀 How to Run

### 🧾 Requirements

- Python **3.8 or higher**
- No external modules required (uses Python Standard Library only)

### 🖥 Execution Steps

1. **Download or copy the project folder**, ensuring `main.py` and JSON files (if present) stay together.

2. **Open Terminal or Command Prompt**
   - Windows: `Win + R → cmd → Enter`
   - Linux/Mac: Open Terminal

3. **Navigate to the project directory**

cd path/to/project

4. **Run the program**

python main.py

*(Use `python3 main.py` if your system requires it.)*

5. **Initial Admin Setup**
- On the first launch, if no admin exists, the system will prompt you to create one.

6. **Login**
- Enter valid credentials to access the system features.

7. **Follow the on-screen menu**
- Enroll students
- Add marks
- Record attendance
- View or delete records (admin only)

8. **Exit**
- All changes remain stored in JSON files for future access.