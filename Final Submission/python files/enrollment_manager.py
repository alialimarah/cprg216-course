"""
EnrollmentManager Class - Course Registration System
=====================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 12, 2025

PURPOSE:
Manages student enrollments in courses. Handles loading/saving enrollment
data and provides operations for registering/dropping students from courses.

RESPONSIBILITIES:
- Load enrollment data from enrollments.csv file
- Save enrollment data back to enrollments.csv file
- Register students in courses (with validation)
- Drop students from courses
- Display student schedules
- Display course rosters
- Check enrollment status
- Assign/update grades

DATA FILE FORMAT (enrollments.csv):
student_id,course_code,semester,grade
2023047891,CPRG216,Fall2024,
2023051234,CPRG251,Fall2024,A

NOTE: grade field is empty until assigned

FILE DEPENDENCIES:
- enrollments.csv (data file)
- student_manager.py (StudentManager class)
- course_manager.py (CourseManager class)

"""


class EnrollmentManager:
    def __init__(self, student_manager, course_manager):
        """
        Initialize the EnrollmentManager.

        Author: [Humza Khan]
        Date: [Dec 11]
        Version: 1.0
        """
        self.student_manager = student_manager
        self.course_manager = course_manager
        self._enrollments = []
        self.read_enrollments_file()
        self.course_manager.update_enrollment_counts(self)

    def read_enrollments_file(self):
        """
        Read enrollment data from enrollments.csv.

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        self._enrollments = []
        try:
            with open("enrollments.csv", "r") as file:
                header = file.readline()
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue

                    parts = line.split(",")
                    if len(parts) < 4:
                        continue

                    student_id = int(parts[0])
                    course_code = parts[1].strip().upper()
                    semester = parts[2].strip()
                    grade = parts[3].strip()

                    enrollment = {
                        "student_id": student_id,
                        "course_code": course_code,
                        "semester": semester,
                        "grade": grade
                    }
                    self._enrollments.append(enrollment)
        except FileNotFoundError:
            self._enrollments = []

    def write_enrollments_to_file(self):
        """
        Write all enrollment data to enrollments.csv file.

        Writes header line followed by all enrollments.

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        with open("enrollments.csv", "w") as file:
            file.write("student_id,course_code,semester,grade\n")
            for e in self._enrollments:
                file.write(f"{e['student_id']},{e['course_code']},{e['semester']},{e['grade']}\n")

    def register_student_in_course(self):
        """
        Register a student in a course through user input.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        student_id_text = input("Enter student ID: ").strip()
        course_code = input("Enter course code: ").strip().upper()
        semester = input("Enter semester (e.g., Fall2024): ").strip()

        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        student = self.student_manager.find_student_by_id(student_id)
        if student is None:
            print("Error: Student does not exist in system")
            return

        course = self.course_manager.find_course_by_code(course_code)
        if course is None:
            print("Error: Course does not exist in system")
            return

        if self.is_student_enrolled_in_course(student_id, course_code):
            print("Error: Student is already enrolled in this course")
            return

        if course.is_full():
            print("Error: Course is full")
            return

        enrollment = {
            "student_id": student_id,
            "course_code": course_code,
            "semester": semester,
            "grade": ""
        }
        self._enrollments.append(enrollment)
        self.course_manager.update_enrollment_counts(self)
        self.write_enrollments_to_file()
        print(f"Student {student.get_full_name()} successfully registered in {course.course_name}")

    def drop_student_from_course(self):
        """
        Drop a student from a course.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        student_id_text = input("Enter student ID: ").strip()
        course_code = input("Enter course code: ").strip().upper()

        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        found = None
        for e in self._enrollments:
            if e["student_id"] == student_id and e["course_code"].upper() == course_code:
                found = e
                break

        if found is None:
            print("Student is not enrolled in this course")
            return

        student = self.student_manager.find_student_by_id(student_id)
        course = self.course_manager.find_course_by_code(course_code)

        self._enrollments.remove(found)
        self.course_manager.update_enrollment_counts(self)
        self.write_enrollments_to_file()

        student_name = student.get_full_name() if student else str(student_id)
        course_name = course.course_name if course else course_code
        print(f"Student {student_name} dropped from {course_name}")

    def display_student_schedule(self):
        """
        Display all courses a student is enrolled in.

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        student_id_text = input("Enter student ID: ").strip()
        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        student = self.student_manager.find_student_by_id(student_id)
        if student is None:
            print("Error: Student does not exist in system")
            return

        enrollments = self.get_student_enrollments(student_id)

        print("=" * 42)
        print(f"SCHEDULE FOR: {student.get_full_name()}")
        print("=" * 42)
        print(f"{'Code':<10}{'Course Name':<25}{'Semester':<12}{'Grade':<5}")
        print("-" * 54)

        total_credits = 0
        for e in enrollments:
            course = self.course_manager.find_course_by_code(e["course_code"])
            course_name = course.course_name if course else ""
            grade = e["grade"]
            if grade == "":
                grade = "-"
            semester = e["semester"]
            print(f"{e['course_code']:<10}{course_name:<25}{semester:<12}{grade:<5}")

            if course:
                total_credits += course.credits

        print("=" * 42)
        print(f"Total Courses: {len(enrollments)}")
        print(f"Total Credits: {total_credits}")

    def display_course_roster(self):
        """
        Display all students enrolled in a course.

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        course_code = input("Enter course code: ").strip().upper()
        course = self.course_manager.find_course_by_code(course_code)
        if course is None:
            print("Error: Course does not exist in system")
            return

        enrollments = self.get_course_enrollments(course_code)

        print("=" * 42)
        print(f"ROSTER FOR: {course.course_code} - {course.course_name}")
        print("=" * 42)
        print(f"{'Student ID':<14}{'Name':<25}{'Year':<6}{'Grade':<5}")
        print("-" * 54)

        for e in enrollments:
            student = self.student_manager.find_student_by_id(e["student_id"])
            name = student.get_full_name() if student else ""
            year = student.year if student else ""
            grade = e["grade"]
            if grade == "":
                grade = "-"
            print(f"{e['student_id']:<14}{name:<25}{year:<6}{grade:<5}")

        print("=" * 42)
        print(f"Enrolled: {len(enrollments)} / {course.capacity}")

    def assign_grade(self):
        """
        Assign or update a grade for a student in a course.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        student_id_text = input("Enter student ID: ").strip()
        course_code = input("Enter course code: ").strip().upper()
        grade = input("Enter grade (A, A-, B+, B, B-, C+, C, C-, D, F): ").strip().upper()

        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        valid_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
        if grade not in valid_grades:
            print("Error: Invalid grade format")
            return

        enrollment = None
        for e in self._enrollments:
            if e["student_id"] == student_id and e["course_code"].upper() == course_code:
                enrollment = e
                break

        if enrollment is None:
            print("Error: Enrollment does not exist")
            return

        enrollment["grade"] = grade
        self.write_enrollments_to_file()

        student = self.student_manager.find_student_by_id(student_id)
        course = self.course_manager.find_course_by_code(course_code)

        student_name = student.get_full_name() if student else str(student_id)
        course_name = course.course_name if course else course_code
        print(f"Grade {grade} assigned to {student_name} for {course_name}")

    def is_student_enrolled_in_course(self, student_id, course_code):
        """
        Check if a student is enrolled in a specific course.

        Returns:
            bool: True if enrolled, False otherwise

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        code = str(course_code).upper()
        for e in self._enrollments:
            if e["student_id"] == student_id and e["course_code"].upper() == code:
                return True
        return False

    def get_student_enrollments(self, student_id):
        """
        Get all enrollments for a specific student.

        Returns:
            list: List of enrollment dictionaries for this student

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        matches = []
        for e in self._enrollments:
            if e["student_id"] == student_id:
                matches.append(e)
        return matches

    def get_course_enrollments(self, course_code):
        """
        Get all enrollments for a specific course.

        Returns:
            list: List of enrollment dictionaries for this course

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        code = str(course_code).upper()
        matches = []
        for e in self._enrollments:
            if e["course_code"].upper() == code:
                matches.append(e)
        return matches

    def get_enrollment_count_for_course(self, course_code):
        """
        Count how many students are enrolled in a course.

        Parameters:
            course_code (str): Course code

        Returns:
            int: Number of students enrolled

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        return len(self.get_course_enrollments(course_code))

    def display_all_enrollments(self):
        """
        Display all enrollments in the system.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        print("=" * 89)
        print("ALL ENROLLMENTS")
        print("=" * 89)
        print(f"{'Student ID':<14}{'Student Name':<22}{'Course Code':<13}{'Course Name':<22}{'Semester':<10}")
        print("-" * 89)

        for e in self._enrollments:
            student = self.student_manager.find_student_by_id(e["student_id"])
            course = self.course_manager.find_course_by_code(e["course_code"])
            student_name = student.get_full_name() if student else ""
            course_name = course.course_name if course else ""
            print(f"{e['student_id']:<14}{student_name:<22}{e['course_code']:<13}{course_name:<22}{e['semester']:<10}")

        print("=" * 89)
        print(f"Total Enrollments: {len(self._enrollments)}")


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_enrollment_manager():
    """Test the EnrollmentManager class implementation."""
    print("=" * 70)
    print("TESTING ENROLLMENT MANAGER CLASS")
    print("=" * 70)
    print()

    # Note: This test requires StudentManager and CourseManager
    # to be implemented first

    from student_manager import StudentManager
    from course_manager import CourseManager

    print("Test 1: Initialize EnrollmentManager...")
    student_mgr = StudentManager()
    course_mgr = CourseManager()
    enrollment_mgr = EnrollmentManager(student_mgr, course_mgr)
    print("✓ Manager created")
    print()

    print("Test 2: Display all enrollments...")
    enrollment_mgr.display_all_enrollments()
    print()


if __name__ == "__main__":
    test_enrollment_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
ENROLLMENT MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 3 points
   [3] Correctly initializes, loads file, updates course counts
   [2] Loads but minor issues
   [1] Partial implementation
   [0] Not implemented

2. File Writing - 2 points
   [2] Correctly writes enrollments to CSV
   [1] Writes but format issues
   [0] Not implemented

3. Register Student Method - 4 points
   [4] All validations work (student exists, course exists, not full, not duplicate)
   [3] Most validations work
   [2] Some validations work
   [1] Registers but no validation
   [0] Not implemented

4. Drop Student Method - 2 points
   [2] Finds enrollment, removes, updates count, saves
   [1] Works but issues
   [0] Not implemented

5. Display Schedule Method - 3 points
   [3] Shows all student courses with formatted table and totals
   [2] Shows courses but formatting/totals issues
   [1] Partial implementation
   [0] Not implemented

6. Display Roster Method - 3 points
   [3] Shows all course students with formatted table
   [2] Shows students but formatting issues
   [1] Partial implementation
   [0] Not implemented

7. Assign Grade Method - 2 points
   [2] Validates enrollment, updates grade, saves
   [1] Works but validation issues
   [0] Not implemented

8. Helper Methods - 1 point
   [1] All helper methods work correctly
   [0] Missing or not working

TOTAL: ___ / 20 points

NOTES:
"""
