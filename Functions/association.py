# class Student:

#     def __init__(self, name):

#         self.name = name
 
 
# class Teacher:

#     def __init__(self, name):

#         self.name = name
 
#     def teach(self, student):

#         print(f"{self.name} teaches {student.name}")
 
 
# # Usage

# student = Student("Rahul")

# teacher = Teacher("Mr. Sharma")
 
# teacher.teach(student)   # Association


class Student:
    def __init__(self, student_id, marks, name):
        self.student_id = student_id
        self.marks = marks
        self.name = name
        self.rank = None
 
    def display(self):
        print(
            f"Student ID: {self.student_id}, "
            f"Student Name: {self.name} "
            f"Marks: {self.marks}, "
            f"Rank: {self.rank}"
        )
 
 
class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.students = []   # HAS-A relationship (Association)
 
    def add_student(self, student):
        self.students.append(student)
 
    def assign_ranks(self):
        # Sort students by marks (highest first)
        self.students.sort(key=lambda s: s.marks, reverse=True)
 
        # Assign ranks
        for i, student in enumerate(self.students, start=1):
            student.rank = i
 
    def display_students(self):
        print(f"\nTeacher ID: {self.teacher_id}")
        print(f"\nTeacher Name: {self.name}")
        print("-" * 40)
        for student in self.students:
            student.display()
 
 
# ---------------- MAIN PROGRAM ----------------
 
# Create Student objects
student1 = Student(101, 95,"Vedant")
student2 = Student(102, 88, "Aman")
student3 = Student(103, 92, "Singh")
 
# Create Teacher object
teacher = Teacher(201, "Rashid")
 
# Association: Teacher HAS students
teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)
 
# Assign ranks based on marks
teacher.assign_ranks()
 
# Display final result
teacher.display_students()