print("SCHOOL RESULT PROCESSING")
name = input("Enter Student Name : ")
roll = input("Enter Roll Number : ")

print("\nEnter Marks for 5 Subjects (0-100)")
total = 0.0
failed_subject = False
valid = True

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        valid = False
        break
    if mark < 40:
        failed_subject = True
    total += mark

if valid:
    percentage = (total / 500) * 100

    if failed_subject:
        result = "FAIL"
        grade = "F"
        remarks = "Failed in one or more subjects"
    else:
        result = "PASS"
        if percentage >= 90:
            grade = "A+"
            remarks = "Outstanding"
        elif percentage >= 80:
            grade = "A"
            remarks = "Excellent"
        elif percentage >= 70:
            grade = "B"
            remarks = "Very Good"
        elif percentage >= 60:
            grade = "C"
            remarks = "Good"
        elif percentage >= 50:
            grade = "D"
            remarks = "Satisfactory"
        elif percentage >= 40:
            grade = "E"
            remarks = "Pass"
        else:
            result = "FAIL"
            grade = "F"
            remarks = "Fail"

    print("\nSTUDENT REPORT CARD")
    print(f"Student Name : {name}")
    print(f"Roll Number : {roll}")
    print(f"\nTotal Marks : {total:.1f} / 500.0")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Result : {result}")
    print(f"Grade : {grade}")
    print(f"Remarks : {remarks}")
