def calculate_grade(average):
    """Return the grade based on the student's average mark."""
    if 90 <= average <= 100:
        return "S"
    elif 80 <= average < 90:
        return "A"
    elif 65 <= average < 80:
        return "B"
    elif 50 <= average < 65:
        return "C"
    elif 40 <= average < 50:
        return "D"
    else:
        return "F"


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("\\n===== STUDENT GRADE MANAGEMENT =====")
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    marks = [get_mark(subject) for subject in subjects]

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("\\n========== STUDENT RESULT ==========")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    for subject, mark in zip(subjects, marks):
        print(f"{subject:<11}: {mark:g}")
    print(f"Total      : {total:g}/300")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")
    print("====================================")


if __name__ == "__main__":
    main()