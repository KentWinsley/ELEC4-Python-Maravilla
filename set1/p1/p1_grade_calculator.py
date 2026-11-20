# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P1 – Student Grade Calculator
# Date: November 19, 2026


def enter_grades():
    grades = []
    while True:
        value = input("Enter a grade (or type done): ").strip()
        if value.lower() == "done":
            if grades:
                return grades
            print("Please enter at least one grade.")
            continue
        try:
            grade = float(value)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a number from 0 to 100.")

def get_average(grades):
    return sum(grades) / len(grades)

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)

def get_status(grades):
    return "PASSED" if get_average(grades) >= 75 else "FAILED"

def show_results(grades):
    print("\n--- GRADE REPORT ---")
    print(f"Average: {get_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest:  {get_lowest(grades):.2f}")
    print(f"Status:  {get_status(grades)}")

def main():
    grades = []
    while True:
        print("\n1. Enter grades\n2. View results\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            if grades:
                show_results(grades)
            else:
                print("Enter grades first.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# In this program, grades inside main() is a local variable because it is created
# inside that function. A local variable can only be used in its function unless
# it is returned or passed to another function. A global variable is created
# outside functions and can be read throughout the file. This program passes
# grades as an argument instead of relying on a global variable.
