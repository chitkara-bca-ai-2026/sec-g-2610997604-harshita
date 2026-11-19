students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": list((85, 90, 78))},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": list((92, 88, 95))},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": list((74, 80, 82))}
}

print("STUDENT INFORMATION MANAGEMENT SYSTEM")

while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\nEnrolled Student Records")
        for roll, info in students.items():
            print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        info = students.get(roll)
        if info:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print(f"Name : {info['Name']}")
            print(f"Branch : {info['Branch']}")
            print(f"Semester : {info['Semester']}")
            print(f"Marks : {info['Marks']}")
        else:
            print(f"\n[ERROR] No student found with Roll No {roll}.")

    elif choice == "3":
        print("\nRegister New Student")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll Number {roll} already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("Subject 1: "))
            m2 = int(input("Subject 2: "))
            m3 = int(input("Subject 3: "))
            students[roll] = {"Name": name, "Branch": branch, "Semester": sem, "Marks": list((m1, m2, m3))}
            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            info = students[roll]
            print(f"Current details for {info['Name']} (Roll {roll}):")
            print(f"1. Branch: {info['Branch']} | 2. Semester: {info['Semester']}")
            field = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if field == "1":
                new_branch = input("Enter new branch: ")
                info["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field == "2":
                new_sem = input("Enter new semester: ")
                info["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid field selection.")
        else:
            print(f"[ERROR] Student with Roll No {roll} not found.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        if roll in students:
            info = students[roll]
            total = sum(info["Marks"])
            avg = total / len(info["Marks"])
            result = "PASS" if avg >= 40 else "FAIL"
            print("\nACADEMIC REPORT")
            print(f"Student Name : {info['Name']} (Roll: {roll})")
            print(f"Subject Marks: {info['Marks']}")
            print(f"Total Marks : {total} / {len(info['Marks']) * 100}")
            print(f"Average Marks: {avg:.2f}%")
            print(f"Final Result : {result}")
        else:
            print(f"[ERROR] Student with Roll No {roll} not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        if removed:
            print(f"\n[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"\n[ERROR] Student with Roll No {roll} not found.")

    elif choice == "7":
        print("\nThank you for using Student Information System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
