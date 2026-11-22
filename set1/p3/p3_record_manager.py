# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P3 – Student Record Manager
# Date: November 22, 2026


students = []

# Adds a student and checks for empty or duplicate names.
def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
    elif name.casefold() in {student.casefold() for student in students}:
        print("That student is already in the list.")
    else:
        students.append(name)
        print(name, "was added.")

# Removes a student by matching the entered name, regardless of uppercase or lowercase.
def remove_student():
    name = input("Name to remove: ").strip()
    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            print(student, "was removed.")
            return
    print("Student not found.")

# Searches for students whose names contain the entered keyword, ignoring case.
def search_student():
    keyword = input("Search name: ").strip().casefold()
    matches = [name for name in students if keyword in name.casefold()]
    if matches:
        for name in matches:
            print("-", name)
    else:
        print("No matching student.")

# Displays all students in alphabetical order, ignoring case, and shows the total count.
def display_students():
    ordered_names = sorted(students, key=str.casefold)
    print(f"\nStudents ({len(ordered_names)} total):")
    for number, name in enumerate(ordered_names, start=1):
        print(f"{number}. {name}")
    if not ordered_names:
        print("No records yet.")

# Display the main menu and allows users to select a student record operation.
def main():
    while True:
        print("\n1. Add\n2. Remove\n3. Search\n4. Display all\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1": add_student()
        elif choice == "2": remove_student()
        elif choice == "3": search_student()
        elif choice == "4": display_students()
        elif choice == "5": break
        else: print("Invalid choice.")

# Starts the student record manager.
if __name__ == "__main__":
    main()

# A list keeps student names in insertion order and allows us to add or remove
# records. A set stores unique values and is useful for checking duplicates.
# In this program, students is a list because we need to manage and display names.
# A temporary set of case-folded names is used when checking for duplicates.
