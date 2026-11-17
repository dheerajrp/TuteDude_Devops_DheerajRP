student_grades = {
    "Aarav": 88,
    "Diya": 92,
    "Rohan": 79
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter new student's name: ")
        if name in student_grades:
            print(f"{name} already exists! Use option 2 to update their grade.")
        else:
            grade = int(input("Enter grade: "))
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")

    elif choice == "2":
        name = input("Enter student's name to update: ")
        if name in student_grades:
            grade = int(input("Enter new grade: "))
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"Student '{name}' not found.")

    elif choice == "3":
        if not student_grades:
            print("No student records found.")
        else:
            print("\nAll Student Grades:")
            for name, grade in student_grades.items():
                print(f"- {name}: {grade}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
