# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P2 – Custom Module: student_utils
# Date: November 21, 2026

# Import built-in and custom modules.
import datetime
import student_utils
from student_utils import calculate_average

def main():
    grades = []

    # Ask the user to input grades until they type "done".
    print("Enter grades from 0 to 100. Type done when finished.")

    # Continue collecting grades until the user types "done".
    while True:
        value = input("Grade: ").strip()
        if value.lower() == "done":
            break

    # Validate the entered grade.
        try:
            grade = float(value)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Invalid number.")
    
    # Check if the user entered any grades.
    if not grades:
        print("No grades entered.")
        return
    
    # Display the student's grade report.
    print("\nSTUDENT REPORT")
    print("Generated:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Average: {calculate_average(grades):.2f}")
    print("Highest:", student_utils.highest_grade(grades))
    print("Lowest:", student_utils.lowest_grade(grades))
    print("Status:", "PASSED" if student_utils.is_passing(grades) else "FAILED")

# Run the main() when this file is executed directly.
if __name__ == "__main__":
    main()
