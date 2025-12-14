"""
StudentManager Class - Course Registration System
==================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 07, 2025

PURPOSE:
Manages the collection of all students in the system. Handles loading/saving
student data from/to CSV file and provides CRUD operations (Create, Read,
Update, Delete) for students.

RESPONSIBILITIES:
- Load student data from students.csv file
- Save student data back to students.csv file
- Add new students to the system
- Remove students from the system
- Search for students by ID or name
- Display student information
- Edit existing student information

FILE DEPENDENCIES:
- students.csv (data file)
- student.py (Student class)

"""

from student import Student


class StudentManager:
    def __init__(self):
        """
        Initialize the StudentManager.

        Creates an empty list of students and loads data from students.csv file.

        Implementation Notes:
        - Initialize empty _students list (private attribute)
        - Call read_students_file() to load existing data

        Author: [Humza Khan]
        Date: [Dec 06]
        Version: 1.0
        """
        self._students = []
        self.read_students_file()

    @property
    def students(self):
        """
        Get the list of all students.

        Returns:
            list: List of Student objects

        Author: [Humza Khan]
        Date: [Dec 06]
        """
        return self._students

    def read_students_file(self):
        """
        Read student data from students.csv and populate the students list.

        File Format:
        student_id,first_name,last_name,email,program,year

        Implementation Notes:
        - Open students.csv for reading
        - Skip the header line
        - For each data line, split by comma and create Student object
        - Add each Student to _students list
        - Handle FileNotFoundError if file doesn't exist

        Author: [Ali Alimarah]
        Date: [Dec 06]
        """
        self._students = []
        try:
            with open("students.csv", "r") as file:
                header = file.readline()
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue

                    parts = line.split(",")
                    if len(parts) != 6:
                        continue

                    student_id = int(parts[0])
                    first_name = parts[1]
                    last_name = parts[2]
                    email = parts[3]
                    program = parts[4]
                    year = int(parts[5])

                    student = Student(student_id, first_name, last_name, email, program, year)
                    self._students.append(student)

        except FileNotFoundError:
            self._students = []

    def write_students_to_file(self):
        """
        Write all student data to students.csv file.

        Writes header line followed by all students in CSV format.

        Implementation Notes:
        - Open students.csv for writing (will overwrite existing)
        - Write header: "student_id,first_name,last_name,email,program,year"
        - For each student, write their to_csv_format() output

        Author: [Ali Alimarah]
        Date: [Dec 06]
        """
        with open("students.csv", "w") as file:
            file.write("student_id,first_name,last_name,email,program,year\n")
            for student in self._students:
                file.write(student.to_csv_format() + "\n")

    def add_student(self):
        """
        Add a new student to the system through user input.

        Prompts user for all student information, creates a new Student
        object, adds it to the list, and saves to file.

        Author: [Humza Khan]
        Date: [Dec 07]
        """
        first_name = input("Enter student's first name: ").strip()
        last_name = input("Enter student's last name: ").strip()
        email = input("Enter student's email: ").strip()
        program = input("Enter student's program: ").strip()
        year_text = input("Enter student's year (1-4): ").strip()

        try:
            year = int(year_text)
            student = Student(None, first_name, last_name, email, program, year)
            self._students.append(student)
            self.write_students_to_file()
            print(f"Student {student.student_id} added successfully!")
        except ValueError:
            print("Error: Invalid year. Student not added.")

    def remove_student(self):
        """
        Remove a student from the system by ID.

        Prompts user for student ID, searches for student, removes if found,
        and saves updated data to file.

        Author: [Humza Khan]
        Date: [Dec 07]
        """
        student_id_text = input("Enter student ID to remove: ").strip()
        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        student = self.find_student_by_id(student_id)
        if student is None:
            print(f"Error: No student found with ID {student_id}")
            return

        self._students.remove(student)
        self.write_students_to_file()
        print(f"Student {student.get_full_name()} (ID: {student.student_id}) removed successfully.")

    def search_student_by_id(self):
        """
        Search for a student by their ID and display their information.

        Author: [Ali Alimarah]
        Date: [Dec 07]
        """
        student_id_text = input("Enter student ID to search: ").strip()
        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return None

        student = self.find_student_by_id(student_id)
        if student:
            self.display_student_info(student)
            return student

        print(f"Error: No student found with ID {student_id}")
        return None

    def search_student_by_name(self):
        """
        Search for students by name (first or last) and display results.

        Searches for partial matches in both first and last names (case-insensitive).

        Author: [Ali Alimarah / Humza Khan]
        Date: [Dec 07]
        """
        term = input("Enter student name to search: ").strip().lower()
        if term == "":
            print("No students found matching ''")
            return

        matches = []
        for student in self._students:
            if term in student.first_name.lower() or term in student.last_name.lower():
                matches.append(student)

        if len(matches) == 0:
            print(f"No students found matching '{term}'")
            return

        print("\n" + "=" * 84)
        print("SEARCH RESULTS")
        print("=" * 84)
        print(f"{'ID':<12}{'Name':<25}{'Email':<30}{'Program':<15}{'Year':<4}")
        print("-" * 84)
        for student in matches:
            name = student.get_full_name()
            program = student.program
            if program is None:
                program = ""
            if len(program) > 14:
                program = program[:14]
            email = student.email
            if email is None:
                email = ""
            print(f"{student.student_id:<12}{name:<25}{email:<30}{program:<15}{student.year:<4}")
        print("=" * 84)
        print(f"Matches: {len(matches)}")

    def edit_student_info(self):
        """
        Edit an existing student's information.

        Author: [Ali Alimarah / Humza Khan]
        Date: [Dec 07]
        """
        student_id_text = input("Enter student ID to edit: ").strip()
        try:
            student_id = int(student_id_text)
        except ValueError:
            print("Error: Invalid student ID")
            return

        student = self.find_student_by_id(student_id)
        if student is None:
            print(f"Error: No student found with ID {student_id}")
            return

        new_first = input("Enter new first name (or press Enter to skip): ")
        if new_first.strip() != "":
            student.first_name = new_first.strip()

        new_last = input("Enter new last name (or press Enter to skip): ")
        if new_last.strip() != "":
            student.last_name = new_last.strip()

        new_email = input("Enter new email (or press Enter to skip): ")
        if new_email.strip() != "":
            student.email = new_email.strip()

        new_program = input("Enter new program (or press Enter to skip): ")
        if new_program.strip() != "":
            student.program = new_program.strip()

        new_year = input("Enter new year 1-4 (or press Enter to skip): ")
        if new_year.strip() != "":
            try:
                student.year = int(new_year.strip())
            except ValueError:
                print("Error: Invalid year. Year not updated.")

        self.write_students_to_file()
        print(f"Student {student.student_id} updated successfully!")

    def display_student_info(self, student):
        """
        Display detailed information for a single student.

        Author: [Humza Khan]
        Date: [Dec 07]
        """
        print("=" * 42)
        print("STUDENT INFORMATION")
        print("=" * 42)
        print(f"Student ID:   {student.student_id}")
        print(f"Name:         {student.first_name} {student.last_name}")
        print(f"Email:        {student.email}")
        print(f"Program:      {student.program}")
        print(f"Year:         {student.year}")
        print("=" * 42)

    def display_students_list(self):
        """
        Display all students in a formatted table.

        Author: [Humza Khan]
        Date: [Dec 07]
        """
        print("=" * 84)
        print("STUDENT LIST")
        print("=" * 84)
        print(f"{'ID':<12}{'Name':<25}{'Email':<30}{'Program':<15}{'Year':<4}")
        print("-" * 84)
        for student in self._students:
            name = student.get_full_name()
            program = student.program
            if program is None:
                program = ""
            if len(program) > 14:
                program = program[:14]
            email = student.email
            if email is None:
                email = ""
            print(f"{student.student_id:<12}{name:<25}{email:<30}{program:<15}{student.year:<4}")
        print("=" * 84)
        print(f"Total Students: {len(self._students)}")

    def get_student_count(self):
        """
        Get the total number of students in the system.

        Returns:
            int: Number of students

        Author: [Ali Alimarah]
        Date: [Dec 07]
        """
        return len(self._students)

    def find_student_by_id(self, student_id):
        """
        Find and return a student by their ID (helper method for other classes).

        Parameters:
            student_id (int): The student ID to search for

        Returns:
            Student or None: The Student object if found, None otherwise

        Author: [Ali Alimarah]
        Date: [Dec 07]
        """
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_student_manager():
    """Test the StudentManager class implementation."""
    print("=" * 70)
    print("TESTING STUDENT MANAGER CLASS")
    print("=" * 70)
    print()

    # Test 1: Initialize and load data
    print("Test 1: Initialize StudentManager...")
    manager = StudentManager()
    print(f"✓ Manager created")
    print(f"  Students loaded: {manager.get_student_count()}")
    print()

    # Test 2: Display all students
    print("Test 2: Display all students...")
    manager.display_students_list()
    print()

    # Test 3: Search by ID
    print("Test 3: Search student by ID...")
    print("Searching for ID: 2023047891")
    manager.search_student_by_id()  # Will prompt for ID in actual use
    print()

    # Test 4: Display single student
    print("Test 4: Display single student info...")
    student = manager.find_student_by_id(2023047891)
    if student:
        manager.display_student_info(student)
    print()


if __name__ == "__main__":
    test_student_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
STUDENT MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 4 points
   [4] Correctly initializes list and loads from file with error handling
   [3] Loads data but minor issues with error handling
   [2] Loads data but has significant issues
   [1] Constructor exists but doesn't load data properly
   [0] Not implemented or doesn't work

2. File Writing - 2 points
   [2] Correctly writes all students to CSV file with proper format
   [1] Writes to file but format issues
   [0] Not implemented or doesn't work

3. Add Student Method - 3 points
   [3] Prompts for all info, creates student, adds to list, saves to file
   [2] Works but missing some functionality
   [1] Partially working
   [0] Not implemented or doesn't work

4. Remove Student Method - 3 points
   [3] Finds student, removes from list, saves file, appropriate messages
   [2] Works but minor issues with error handling or messages
   [1] Partially working
   [0] Not implemented or doesn't work

5. Search Methods (by ID and by name) - 4 points
   [4] Both search methods work correctly with appropriate error messages
   [3] Both work but minor issues
   [2] One search method works correctly
   [1] Partially implemented
   [0] Not implemented or doesn't work

6. Edit Student Method - 2 points
   [2] Allows editing all fields, handles empty input, saves changes
   [1] Works but has issues
   [0] Not implemented or doesn't work

7. Display Methods - 2 points
   [2] Both display methods format output nicely and correctly
   [1] Display works but formatting issues
   [0] Not implemented or doesn't work

TOTAL: ___ / 20 points

NOTES:
"""