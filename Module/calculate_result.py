def calculate_result():
    name = input("Enter student name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / subjects

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    if average >= 75:
        grade = "DISTINCTION"
    elif average >= 60:
        grade = "FIRST CLASS"
    elif average >= 40:
        grade = "SECOND CLASS"
    else:
        grade = "NO GRADE"

    print("\n----- Student Report -----")
    print(f"Name       : {name}")
    print(f"Total Marks: {total}")
    print(f"Average    : {average:.2f}")
    print(f"Result     : {result}")
    print(f"Grade      : {grade}")
