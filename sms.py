import json
import os  # Needed to check if files exist

stud_file = "students.json"
user_file = "users.json"

def load_data(filename):            #STUDENT DATA MANAGEMENT(NUMBER: 1)
    """
    Checks if file exists first.
    If YES - Open and read.
    If NO  - Return empty dictionary.
    """
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    return {}

def save_data(filename, data):
    """Saves data to the file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def ensure_admin_exists(users):                 #CHECKS ADMIN AUTHENTICATION(NUMBER: 2)
    """Checks if admin exists, forces creation if missing."""
    admin_found = False
    for user_data in users.values():
        if user_data.get("role") == "admin":
            admin_found = True
            break
    
    if not admin_found:
        print("\n========================================")
        print("         SYSTEM INITIALIZATION          ")
        print("========================================")
        print("[SYSTEM] First run detected.")
        print("Please create the System Administrator account.")
        
        while True:
            username = input("\nSet Admin Username: ").strip()
            if not username:
                print("Username cannot be empty.")
                continue
            
            pw1 = input("Set Password: ").strip()
            pw2 = input("Confirm Password: ").strip()
            
            if pw1 == pw2 and pw1:
                users[username] = {"password": pw1, "role": "admin"}
                save_data(user_file, users)
                print(">> Admin created successfully.\n")
                break
            else:
                print("Passwords do not match.")

def login(users):
    print("\n========================================")
    print("                 LOGIN                  ")
    print("========================================")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if username in users:
        if users[username]["password"] == password:
            print(f">> Welcome, {username}!")
            return {"name": username, "role": users[username]["role"]}
    
    print(">> Invalid credentials.\n")
    return None

def enroll_student():               #STUDENT MANAGEMENT(NUMBER: 3)
    students = load_data(stud_file)
    print("\n========================================")
    print("           ENROLL NEW STUDENT           ")
    print("========================================")
    
    reg_no = input("Registration No: ").strip()
    if not reg_no.isdigit():
        print(">> Error: Registration must be digits.")
        return
    if reg_no in students:
        print(">> Error: Student already exists.")
        return
        
    name = input("Name: ").strip()
    batch = input("Batch(EX-2029): ").strip()
    branch = input("Branch(EX-AIML): ").strip()
    
    n_sub_str = input("Number of subjects: ").strip()
    if not n_sub_str.isdigit():
        print(">> Invalid number.")
        return
        
    subjects = {}
    for i in range(int(n_sub_str)):
        sub_name = input(f"Subject #{i+1} Name: ").strip()
        subjects[sub_name] = {"marks": {}, "attendance": {}}

    students[reg_no] = {
        "name": name,
        "reg_no": reg_no,
        "batch": batch,
        "branch": branch,
        "subjects": subjects
    }
    save_data(stud_file, students)
    print(f">> Enrolled {name}.\n")

def view_students():
    students = load_data(stud_file)
    print("\n========================================")
    print("              VIEW RECORDS              ")
    print("========================================")
    reg = input("Search Registration Number (Enter for all): ").strip()
    
    found = False
    for key, data in students.items():
        if reg == "" or key == reg:
            found = True
            print("-" * 40)
            print(f"[Reg: {key}] {data['name']} | {data['branch']}")
            for sub, details in data["subjects"].items():
                print(f"   - {sub}: Marks {details['marks']}, Att Days {len(details['attendance'])}")
    
    if not found:
        print(">> No records found.")
    print("-" * 40)
    print("")

def delete_student(current_user):
    if current_user["role"] != "admin":
        print(">> Access Denied.\n")
        return
    
    print("\n========================================")
    print("             DELETE STUDENT             ")
    print("========================================")
    
    students = load_data(stud_file)
    reg_no = input("Delete Registration Number: ").strip()
    
    if reg_no in students:
        confirm = input("Type 'YES' to confirm: ").strip()
        if confirm == "YES":
            del students[reg_no]
            save_data(stud_file, students)
            print(">> Deleted.\n")
    else:
        print(">> Not found.\n")

def add_marks():                        #ACADEMIC OPERATIONS(NUMBER: 4)
    students = load_data(stud_file)
    print("\n========================================")
    print("               ADD MARKS                ")
    print("========================================")
    reg_no = input("Enter Registration Number: ").strip()
    
    if reg_no not in students:
        print(">> Student not found.")
        return
        
    student = students[reg_no]
    sub = input(f"Subject ({', '.join(student['subjects'].keys())}): ").strip()
    
    if sub in student["subjects"]:
        exam = input("Exam Type(MID TERM/ TERM END): ").strip()
        score_str = input("Marks: ").strip()
        
        if score_str.replace('.', '', 1).isdigit():             # Manual float check
            student["subjects"][sub]["marks"][exam] = float(score_str)
            save_data(stud_file, students)
            print(">> Saved.")
        else:
            print(">> Error: Marks must be a number.")
    else:
        print(">> Subject not found.")

def mark_attendance():
    students = load_data(stud_file)
    print("\n========================================")
    print("            MARK ATTENDANCE             ")
    print("========================================")
    reg_no = input("Enter Registration Number: ").strip()
    
    if reg_no not in students:
        print(">> Student not found.")
        return
        
    student = students[reg_no]
    sub = input(f"Subject ({', '.join(student['subjects'].keys())}): ").strip()
    
    if sub in student["subjects"]:
        date = input("Date (YYYY-MM-DD): ").strip()
        status = input("Status (P/A): ").strip().upper()
        
        if status in ["P", "A"]:
            student["subjects"][sub]["attendance"][date] = status
            save_data(stud_file, students)
            print(">> Recorded.")
        else:
            print(">> Invalid status.")
    else:
        print(">> Subject not found.")

def main_menu(user):                        #MAIN METHOD(NUMBER: 5)
    while True:
        print("\n========================================")
        print(f"      DASHBOARD: {user['name'].upper()}")
        print("========================================")
        print("1. Enroll New Student")
        print("2. View Records")
        print("3. Add Marks")
        print("4. Mark Attendance")
        if user["role"] == "admin":
            print("9. Delete Student")
        print("0. Logout")
        
        ch = input("\nChoice: ").strip()
        
        if ch == "1": enroll_student()
        elif ch == "2": view_students()
        elif ch == "3": add_marks()
        elif ch == "4": mark_attendance()
        elif ch == "9": delete_student(user)
        elif ch == "0": break
        else: print("Invalid option.")

def main():
    users = load_data(user_file)
    ensure_admin_exists(users)
    users = load_data(user_file)
    
    while True:
        print("\n========================================")
        print("       STUDENT MANAGEMENT SYSTEM        ")
        print("========================================")
        print("1. Login")
        print("0. Exit")
        ch = input("\n>> ").strip()
        
        if ch == "1":
            user = login(users)
            if user:
                main_menu(user)
                users = load_data(user_file)
        elif ch == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()