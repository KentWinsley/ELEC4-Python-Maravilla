# Name: Kent Winsley R. Maravilla
# Section: IV-BSIT-C
# Activity: P2 – Custom Module: student_utils
# Date: November 21, 2026

# Calculate the average of the grades.
def calculate_average(grades):
    return sum(grades) / len(grades)

# Check if the average grade is passing.
def is_passing(grades):
    return calculate_average(grades) >= 75

# Get the highest grade.
def highest_grade(grades):
    return max(grades)

# Get the lowest grade.
def lowest_grade(grades):
    return min(grades)
