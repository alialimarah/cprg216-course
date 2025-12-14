"""
Main Application - Course Registration System
==============================================

TEAM MEMBER ASSIGNED TO THIS FILE:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 13, 2025

PURPOSE:
Main entry point for the Course Registration System. Provides menu-based
interface for accessing all system functions.

RESPONSIBILITIES:
- Initialize all manager objects
- Display main menu and submenus
- Route user selections to appropriate manager methods
- Handle program flow and user navigation
- Provide clean exit

FILE DEPENDENCIES:
- student_manager.py (StudentManager class)
- course_manager.py (CourseManager class)
- enrollment_manager.py (EnrollmentManager class)

"""

from student_manager import StudentManager
from course_manager import CourseManager
from enrollment_manager import EnrollmentManager


class RegistrationSystem:
    def __init__(self):
        """
        Initialize the Registration System.

        Creates all manager objects and links them together.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        Version: 1.0
        """
        print("=" * 70)
        print("COURSE REGISTRATION SYSTEM")
        print("Initializing...")
        print("=" * 70)

        self.student_manager = StudentManager()
        self.course_manager = CourseManager()
        self.enrollment_manager = EnrollmentManager(self.student_manager, self.course_manager)

        print("✓ System initialized successfully!")
        print()

    def display_main_menu(self):
        """
        Display the main menu and handle user selection.

        Author: [Ali Alimarah]
        Date: [Dec 12]
        """
        while True:
            print("=" * 70)
            print("MAIN MENU")
            print("=" * 70)
            print("1 - Student Management")
            print("2 - Course Management")
            print("3 - Enrollment Management")
            print("4 - Reports")
            print("5 - Exit Program")
            print("=" * 70)

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.display_student_menu()
            elif choice == "2":
                self.display_course_menu()
            elif choice == "3":
                self.display_enrollment_menu()
            elif choice == "4":
                self.display_reports_menu()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def display_student_menu(self):
        """
        Display the student management submenu.

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        while True:
            print("\n" + "=" * 70)
            print("STUDENT MANAGEMENT")
            print("=" * 70)
            print("1 - Display all students")
            print("2 - Search student by ID")
            print("3 - Search student by name")
            print("4 - Add new student")
            print("5 - Edit student information")
            print("6 - Remove student")
            print("7 - Return to main menu")
            print("=" * 70)

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.student_manager.display_students_list()
            elif choice == "2":
                self.student_manager.search_student_by_id()
            elif choice == "3":
                self.student_manager.search_student_by_name()
            elif choice == "4":
                self.student_manager.add_student()
            elif choice == "5":
                self.student_manager.edit_student_info()
            elif choice == "6":
                self.student_manager.remove_student()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

    def display_course_menu(self):
        """
        Display the course management submenu.

        Author: [Humza Khan]
        Date: [Dec 12]
        """
        while True:
            print("\n" + "=" * 70)
            print("COURSE MANAGEMENT")
            print("=" * 70)
            print("1 - Display all courses")
            print("2 - Search course by code")
            print("3 - Search courses by name")
            print("4 - Add new course")
            print("5 - Edit course information")
            print("6 - Remove course")
            print("7 - Return to main menu")
            print("=" * 70)

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.course_manager.display_courses_list()
            elif choice == "2":
                self.course_manager.search_course_by_code()
            elif choice == "3":
                self.course_manager.search_courses_by_name()
            elif choice == "4":
                self.course_manager.add_course()
            elif choice == "5":
                self.course_manager.edit_course_info()
            elif choice == "6":
                self.course_manager.remove_course()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

    def display_enrollment_menu(self):
        """
        Display the enrollment management submenu.

        Author: [Ali Alimarah]
        Date: [Dec 13]
        """
        while True:
            print("\n" + "=" * 70)
            print("ENROLLMENT MANAGEMENT")
            print("=" * 70)
            print("1 - Register student in course")
            print("2 - Drop student from course")
            print("3 - Display student schedule")
            print("4 - Display course roster")
            print("5 - Assign grade")
            print("6 - Return to main menu")
            print("=" * 70)

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.enrollment_manager.register_student_in_course()
            elif choice == "2":
                self.enrollment_manager.drop_student_from_course()
            elif choice == "3":
                self.enrollment_manager.display_student_schedule()
            elif choice == "4":
                self.enrollment_manager.display_course_roster()
            elif choice == "5":
                self.enrollment_manager.assign_grade()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

    def display_reports_menu(self):
        """
        Display the reports submenu.

        Author: [Ali Alimarah]
        Date: [Dec 13]
        """
        while True:
            print("\n" + "=" * 70)
            print("REPORTS")
            print("=" * 70)
            print("1 - All enrollments")
            print("2 - System statistics")
            print("3 - Return to main menu")
            print("=" * 70)

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                self.enrollment_manager.display_all_enrollments()
            elif choice == "2":
                self.display_statistics()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

    def display_statistics(self):
        """
        Display system statistics.

        Author: [Humza Khan]
        Date: [Dec 13]
        """
        print("\n" + "=" * 70)
        print("SYSTEM STATISTICS")
        print("=" * 70)

        total_students = self.student_manager.get_student_count()
        total_courses = self.course_manager.get_course_count()
        total_enrollments = len(self.enrollment_manager._enrollments)

        if total_courses > 0:
            avg_students_per_course = total_enrollments / total_courses
        else:
            avg_students_per_course = 0

        top_course = None
        for course in self.course_manager.courses:
            if top_course is None:
                top_course = course
            else:
                if course.enrolled_count > top_course.enrolled_count:
                    top_course = course

        print(f"Total Students: {total_students}")
        print(f"Total Courses: {total_courses}")
        print(f"Total Enrollments: {total_enrollments}")
        print(f"Average Students per Course: {avg_students_per_course:.2f}")

        if top_course:
            print(f"Highest Enrollment Course: {top_course.course_code} - {top_course.course_name} ({top_course.enrolled_count} students)")
        else:
            print("Highest Enrollment Course: N/A")

        print("=" * 70)

    def run(self):
        """
        Start the registration system.

        Entry point for the application. Displays welcome message
        and starts the main menu loop.

        Author: [Humza Khan]
        Date: [Dec 13]
        """
        print("\n" + "=" * 70)
        print("WELCOME TO THE COURSE REGISTRATION SYSTEM")
        print("=" * 70)
        print()

        self.display_main_menu()

        # When user exits
        print("\n" + "=" * 70)
        print("Thank you for using the Course Registration System!")
        print("=" * 70)


# ==============================================================================
# PROGRAM ENTRY POINT (Do not modify)
# ==============================================================================

def main():
    """
    Main function - creates and runs the registration system.
    """
    system = RegistrationSystem()
    system.run()


if __name__ == "__main__":
    main()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
MAIN APPLICATION RUBRIC (20 points total)

1. System Initialization - 3 points
   [3] All managers created and linked correctly
   [2] Managers created but linking issues
   [1] Partial initialization
   [0] Not implemented

2. Main Menu - 3 points
   [3] Menu displays correctly, routes to all submenus, handles invalid input
   [2] Works but minor issues
   [1] Partial functionality
   [0] Not implemented

3. Student Management Menu - 3 points
   [3] All 7 options work correctly, proper routing to student_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

4. Course Management Menu - 3 points
   [3] All 7 options work correctly, proper routing to course_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

5. Enrollment Management Menu - 3 points
   [3] All 6 options work correctly, proper routing to enrollment_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

6. Reports Menu - 3 points
   [3] Both reports work correctly with accurate statistics
   [2] Reports work but calculation issues
   [1] One report works
   [0] Not implemented

7. User Experience - 2 points
   [2] Clean interface, clear messages, error handling throughout
   [1] Functional but UX issues
   [0] Poor or no error handling

TOTAL: ___ / 20 points

NOTES:
"""
