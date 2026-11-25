# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P5 - Student Information File System
# Date: November 25, 2026

from pathlib import Path

FILE_NAME = Path(__file__).with_name("students.txt")


# Load existing student records from the text file.
def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                record = line.strip().split("|")

                if len(record) == 4:
                    students.append(record)

    except FileNotFoundError:
        print("No students.txt found. Starting with empty records.")

    return students


# Add a new student and append the record to the file.
def add_student(students):
    student_id = input("Student ID: ").strip()

    # Check if the ID already exists.
    for student in students:
        if student[0] == student_id:
            print("Student ID already exists.")
            return

    name = input("Full name: ").strip()
    section = input("Course/Section: ").strip()

    try:
        average = float(input("General average: "))

        if average < 0 or average > 100:
            print("Average must be from 0 to 100.")
            return

    except ValueError:
        print("Invalid input. Average must be a number.")
        return

    record = [student_id, name, section, str(average)]

    # Append the new record without replacing existing records.
    try:
        with open(FILE_NAME, "a") as file:
            file.write("|".join(record) + "\n")

        students.append(record)
        print("Student added successfully.")

    except OSError:
        print("Error saving student record.")


# Display all student records.
def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- ALL STUDENTS ---")

    for student in students:
        print(
            f"ID: {student[0]} | Name: {student[1]} | "
            f"Section: {student[2]} | Average: {student[3]}"
        )


# Search for a student using their ID.
def search_student(students):
    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student[0] == student_id:
            print("\nStudent found:")
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Section: {student[2]}")
            print(f"Average: {student[3]}")
            return

    print("Student not found.")


# Update an existing student's information.
def update_student(students):
    student_id = input("Enter student ID to update: ").strip()

    for student in students:
        if student[0] == student_id:
            print("Leave a field blank to keep its current value.")

            name = input(f"Full name [{student[1]}]: ").strip()
            section = input(f"Section [{student[2]}]: ").strip()
            average_text = input(f"Average [{student[3]}]: ").strip()

            # Check the new average before changing the record.
            if average_text:
                try:
                    average = float(average_text)

                    if average < 0 or average > 100:
                        print("Average must be from 0 to 100.")
                        return

                except ValueError:
                    print("Invalid input. Average must be a number.")
                    return

            # Apply the changes if the inputs are valid.
            if name:
                student[1] = name

            if section:
                student[2] = section

            if average_text:
                student[3] = str(average)

            # Rewrite the file to save the updated records.
            try:
                with open(FILE_NAME, "w") as file:
                    for record in students:
                        file.write("|".join(record) + "\n")

                print("Student information updated.")

            except OSError:
                print("Error updating the file.")

            return

    print("Student not found.")


# Load records and display the menu until the user exits.
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT INFORMATION SYSTEM =====")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student by ID")
        print("4. Update student information")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please choose 1 to 5.")


if __name__ == "__main__":
    main()