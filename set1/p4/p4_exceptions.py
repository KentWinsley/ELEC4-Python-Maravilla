# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P4 – Safe Menu Program
# Date: November 22, 2026

# Function to divide two numbers with exception handling.
def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        answer = first / second
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print("Answer:", answer)
    finally:
        print("Division option finished.")

# This function allows users to read the contents of a text file.
def read_file():
    filename = input("File name to open: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("That file does not exist.")
    except PermissionError:
        print("You do not have permission to read that file.")
    else:
        print("\n--- FILE CONTENTS ---")
        print(content if content else "(File is empty.)")
    finally:
        print("File option finished.")

# Main menu of the program.
def main():
    while True:
        print("\n1. Divide two numbers\n2. Open a text file\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            read_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Select 1, 2, or 3.")

# Start the program.
if __name__ == "__main__":
    main()
