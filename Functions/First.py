def greet_student(name):
    """
    Function to greet a student.
    """
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
    """
    Function to calculate total marks.
    """
    return sum(marks)


def calculate_average(total, count):
    """
    Function to calculate average marks.
    """
    return total / count


def check_result(average):
    """
    Function to determine pass or fail.
    """
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    """
    Main function that calls other functions.
    """
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


# Program execution starts here
if __name__ == "__main__":
    student_name = "Rashid"
    student_marks = [65, 70, 55, 80, 60]

    # ✅ CALL THE FUNCTION
    display_result(student_name, student_marks)
