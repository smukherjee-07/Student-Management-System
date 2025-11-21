# 🎓 STUDENT MANAGEMENT SYSTEM (SMS)

## 📑 Synopsis

The *Student Management System* is a console-based application designed to streamline and automate academic record management in an educational institution. It replaces traditional paper-based entries with a structured, persistent digital storage system using *Python* and *JSON*.

The system features automatic database initialization during the first execution, a clear data flow architecture, and *Role-Based Access Control (RBAC)* to distinguish administrative privileges from standard user operations.

## ⚙ System Architecture

The application follows a modular structure where each functional unit is responsible for a specific task. All operations adhere to the pipeline:

*User Input → Data Validation → In-Memory Processing → JSON Data Storage*

### 1. Data Persistence Layer

Two JSON files store all essential data permanently:

- **users.json** — Contains authentication credentials and user roles.
- **students.json** — Stores student profiles, subjects, marks, and attendance in a nested dictionary structure.

This approach ensures data reliability across multiple sessions.

### 2. Core Functional Modules

#### A. Database Handlers

- **load_data(filename)**  
  Checks for file existence before attempting to read it. If the file is missing, it safely returns an empty dictionary, preventing runtime errors.

- **save_data(filename, data)**  
  Writes in-memory data into JSON files with indentation for readability.

#### B. Authentication System

- **ensure_admin_exists(users)**  
  During the first run, the system verifies whether an admin account exists. If not, it prompts the user to create one before proceeding.

- **login(users)**  
  Validates user credentials and returns the corresponding role (Admin/User).

#### C. Student Operations (CRUD)

- **enroll_student()**  
  Adds new student records with proper validation for registration numbers and prevents duplicate entries. Subjects are added dynamically based on user input.

- **view_students()**  
  Displays all student records or searches specific entries using Registration ID through a linear lookup method.

- **delete_student()**  
  Restricted to admin users. Securely removes student records from the database.

#### D. Academic Module

- **add_marks()**  
  Updates student marks with strict validation to avoid incorrect or invalid entries.

- **mark_attendance()**  
  Records attendance along with timestamps to maintain an accurate academic log.

## 🚀 Execution Instructions

### Prerequisites

- Python 3.8 or higher  
- No external libraries required (Standard Library only)

### How to Run

1. Open a terminal inside the project directory.  
2. Execute the command:
   ```bash
   python main.py
3. On the first run, if the database files are missing, the system will automatically generate them and prompt for the creation of an initial administrator account..
