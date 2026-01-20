# ==============================
# Student Management System (Improved)
# ==============================

from dataclasses import dataclass
from typing import Dict, List, Optional


# ---------- SAFE INPUT FUNCTIONS ----------

def get_int_input(message: str) -> int:
    while True:
        raw = input(message).strip()
        try:
            return int(raw)
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")


def get_marks_input(message: str) -> int:
    while True:
        raw = input(message).strip()
        try:
            marks = int(raw)
            if 0 <= marks <= 100:
                return marks
            print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter numeric marks (0-100).")


def get_name_input(message: str) -> str:
    while True:
        name = input(message).strip()
        if name:
            return name
        print("❌ Name cannot be empty.")


# ---------- STUDENT MODEL ----------

@dataclass
class Student:
    student_id: int
    name: str
    marks: int
    result: str = ""
    rank: Optional[int] = None

    def __post_init__(self):
        self.update_result()

    def update_result(self):
        self.result = "PASS" if self.marks >= 35 else "FAIL"

    def display(self):
        rank_str = "-" if self.rank is None else str(self.rank)
        print(
            f"ID: {self.student_id:<6} | "
            f"Name: {self.name:<20} | "
            f"Marks: {self.marks:<3} | "
            f"Result: {self.result:<4} | "
            f"Rank: {rank_str}"
        )


# ---------- TEACHER CLASS (MANAGEMENT) ----------

class Teacher:
    AUTO_DELETE_THRESHOLD = 20

    def __init__(self, teacher_id: int, name: str):
        self.teacher_id = teacher_id
        self.name = name
        self._students: Dict[int, Student] = {}

    # --- CRUD operations ---

    def add_student(self, student: Student) -> None:
        if student.marks < self.AUTO_DELETE_THRESHOLD:
            print(f"❌ Marks < {self.AUTO_DELETE_THRESHOLD}. Student auto-deleted / not added.")
            return

        if student.student_id in self._students:
            print("❌ Student with this ID already exists.")
            return

        student.name = student.name.strip()
        self._students[student.student_id] = student
        print("✅ Student added successfully.")
        self.assign_ranks()

    def delete_student(self, student_id: int) -> None:
        if student_id in self._students:
            del self._students[student_id]
            print("✅ Student deleted successfully.")
            self.assign_ranks()
        else:
            print("❌ Student not found.")

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        return self._students.get(student_id)

    def update_student_marks(self, student_id: int, new_marks: int) -> None:
        student = self.get_student_by_id(student_id)
        if not student:
            print("❌ Student not found.")
            return

        if new_marks < self.AUTO_DELETE_THRESHOLD:
            del self._students[student_id]
            print(f"❌ Marks < {self.AUTO_DELETE_THRESHOLD}. Student auto-deleted.")
            self.assign_ranks()
            return

        student.marks = new_marks
        student.update_result()
        print("✅ Marks updated successfully.")
        self.assign_ranks()

    # --- Search ---

    def search_by_name(self, name: str) -> None:
        name = name.strip().lower()
        found = [s for s in self._students.values() if s.name.lower() == name]
        if not found:
            print("❌ Student not found.")
            return
        for s in found:
            s.display()

    # --- Display ---

    def display_students(self) -> None:
        students = self.all_students()
        if not students:
            print("⚠️ No students available.")
            return

        print(f"\nTeacher: {self.name} (ID: {self.teacher_id})")
        print(f"Total Strength: {self.total_strength()}")
        print("-" * 80)

        # PASS first (higher marks first), then FAIL (higher marks first)
        sorted_students = sorted(
            students,
            key=lambda s: (s.result == "FAIL", -s.marks, s.student_id)
        )

        for student in sorted_students:
            student.display()

    # --- Ranking & stats ---

    def all_students(self) -> List[Student]:
        return list(self._students.values())

    def assign_ranks(self) -> None:
        passed = [s for s in self._students.values() if s.result == "PASS"]
        passed.sort(key=lambda s: (-s.marks, s.student_id))

        # Tie-aware ranking: same marks => same rank
        rank = 0
        prev_marks = None
        for idx, s in enumerate(passed, start=1):
            if prev_marks != s.marks:
                rank = idx
                prev_marks = s.marks
            s.rank = rank

        for s in self._students.values():
            if s.result == "FAIL":
                s.rank = None

    def total_strength(self) -> int:
        return len(self._students)

    def average_marks(self) -> float:
        students = self.all_students()
        if not students:
            return 0.0
        return sum(s.marks for s in students) / len(students)

    def highest_marks(self) -> Optional[Student]:
        students = self.all_students()
        return max(students, key=lambda s: s.marks, default=None)

    def lowest_marks(self) -> Optional[Student]:
        students = self.all_students()
        return min(students, key=lambda s: s.marks, default=None)


# ---------- MAIN PROGRAM ----------

def print_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Search Student by ID")
    print("6. Search Student by Name")
    print("7. Statistics")
    print("8. Exit")


def show_statistics(teacher: Teacher):
    print(f"\nAverage Marks: {teacher.average_marks():.2f}")

    high = teacher.highest_marks()
    low = teacher.lowest_marks()

    if high:
        print("\nTop Scorer:")
        high.display()
    else:
        print("\nTop Scorer: -")

    if low:
        print("\nLowest Scorer:")
        low.display()
    else:
        print("\nLowest Scorer: -")


def main():
    teacher = Teacher(201, "Rashid")

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            sid = get_int_input("Student ID: ")
            name = get_name_input("Student Name: ")
            marks = get_marks_input("Marks: ")
            teacher.add_student(Student(sid, name, marks))

        elif choice == "2":
            teacher.display_students()

        elif choice == "3":
            sid = get_int_input("Student ID: ")
            marks = get_marks_input("New Marks: ")
            teacher.update_student_marks(sid, marks)

        elif choice == "4":
            sid = get_int_input("Student ID: ")
            teacher.delete_student(sid)

        elif choice == "5":
            sid = get_int_input("Student ID: ")
            student = teacher.get_student_by_id(sid)
            if student:
                student.display()
            else:
                print("❌ Student not found.")

        elif choice == "6":
            name = get_name_input("Student Name: ")
            teacher.search_by_name(name)

        elif choice == "7":
            show_statistics(teacher)

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please select from 1 to 8.")


if __name__ == "__main__":
    main()