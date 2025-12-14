"""
Student Class - Course Registration System
===========================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 06, 2025

PURPOSE:
Represents a single student in the system with their personal information
and academic details.

RESPONSIBILITIES:
- Store student information (ID, name, email, program, year)
- Provide access to student data through properties
- Format student information for display and file storage
- Validate student data

DATA FILE FORMAT (students.csv):
student_id,first_name,last_name,email,program,year
2023047891,Sarah,Johnson,sarah.johnson@mystudent.ca,Computer Programming,1

"""

import random


class Student:
    def __init__(self, student_id=None, first_name=None, last_name=None,
                 email=None, program=None, year=None):
        """
        Author: [Humza Khan]
        Date: [Dec 04]
        Version: 1.0
        """
        self._student_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._program = None
        self._year = None

        if student_id is None:
            student_id = random.randint(2023000000, 2023999999)

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.program = program
        self.year = year

    @property
    def student_id(self):
        """
        Get the student's ID.

        Author: [Humza Khan]
        Date: [Dec 04]
        """
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        """
        Set the student's ID.

        Author: [Ali Alimarah]
        Date: [Dec 04]
        """
        if value is None:
            raise ValueError("Student ID cannot be None")

        value = int(value)
        if value < 1000000000 or value > 9999999999:
            raise ValueError("Student ID must be a 10-digit number")

        self._student_id = value

    @property
    def first_name(self):
        """
        Get the student's first name.

        Returns:
            str: Student's first name

        Author: [Ali Alimarah]
        Date: [Dec 04]
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Set the student's first name.

        Parameters:
            value (str): New first name

        Author: [Humza Khan]
        Date: [Dec 04]
        """
        self._first_name = value

    @property
    def last_name(self):
        """
        Get the student's last name.

        Returns:
            str: Student's last name

        Author: [Humza Khan]
        Date: [Dec 04]
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Set the student's last name.

        Parameters:
            value (str): New last name

        Author: [Ali Alimarah]
        Date: [Dec 05]
        """
        self._last_name = value

    @property
    def email(self):
        """
        Get the student's email address.

        Returns:
            str: Student's email

        Author: [Ali Alimarah]
        Date: [Dec 05]
        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Set the student's email address.

        Parameters:
            value (str): New email address

        Author: [Humza Khan]
        Date: [Dec 05]
        """
        self._email = value

    @property
    def program(self):
        """
        Get the student's academic program.

        Returns:
            str: Name of academic program

        Author: [Humza Khan]
        Date: [Dec 05]
        """
        return self._program

    @program.setter
    def program(self, value):
        """
        Set the student's academic program.

        Parameters:
            value (str): New program name

        Author: [Ali Alimarah]
        Date: [Dec 05]
        """
        self._program = value

    @property
    def year(self):
        """
        Get the student's current year in program.

        Returns:
            int: Year (1, 2, 3, or 4)

        Author: [Ali Alimarah]
        Date: [Dec 05]
        """
        return self._year

    @year.setter
    def year(self, value):
        """
        Set the student's current year in program.

        Author: [Humza Khan]
        Date: [Dec 05]
        """
        if value is None:
            self._year = value
            return

        value = int(value)
        if value < 1 or value > 4:
            raise ValueError("Year must be between 1 and 4")

        self._year = value

    def __str__(self):
        """
        Return a formatted string representation of the student.

        Author: [Humza Khan]
        Date: [Dec 05]
        """
        return f"ID: {self.student_id} | Name: {self.first_name} {self.last_name} | Program: {self.program} (Year {self.year})"

    def to_csv_format(self):
        """
        Format student data for CSV file storage.

        Returns comma-separated values matching the CSV header:
        student_id,first_name,last_name,email,program,year

        Example:
        "2023047891,Sarah,Johnson,sarah.johnson@mystudent.ca,Computer Programming,1"

        Returns:
            str: CSV-formatted string

        Author: [Ali Alimarah]
        Date: [Dec 05]
        """
        return f"{self.student_id},{self.first_name},{self.last_name},{self.email},{self.program},{self.year}"

    def get_full_name(self):
        """
        Get the student's full name.

        Returns:
            str: Full name in format "First Last"

        Author: [Ali Alimarah]
        Date: [Dec 06]
        """
        return f"{self.first_name} {self.last_name}"


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_student_class():
    """Test the Student class implementation."""
    print("=" * 70)
    print("TESTING STUDENT CLASS")
    print("=" * 70)
    print()

    # Test 1: Create student with all parameters
    print("Test 1: Creating student with all parameters...")
    s1 = Student(2023047891, "Sarah", "Johnson",
                 "sarah.johnson@mystudent.ca", "Computer Programming", 1)
    print(f"✓ Student created: {s1}")
    print()

    # Test 2: Create student with auto-generated ID
    print("Test 2: Creating student with auto-generated ID...")
    s2 = Student(first_name="Michael", last_name="Chen",
                 email="michael.chen@mystudent.ca",
                 program="Software Development", year=2)
    print(f"✓ Student created: {s2}")
    print(f"  Auto-generated ID: {s2.student_id}")
    print()

    # Test 3: Test property access
    print("Test 3: Testing property access...")
    print(f"  First Name: {s1.first_name}")
    print(f"  Last Name: {s1.last_name}")
    print(f"  Email: {s1.email}")
    print(f"  Program: {s1.program}")
    print(f"  Year: {s1.year}")
    print()

    # Test 4: Test property modification
    print("Test 4: Testing property modification...")
    s1.program = "Information Technology"
    s1.year = 2
    print(f"✓ Modified: {s1}")
    print()

    # Test 5: Test CSV format
    print("Test 5: Testing CSV format...")
    print(f"  CSV: {s1.to_csv_format()}")
    print()

    # Test 6: Test full name
    print("Test 6: Testing full name...")
    print(f"  Full Name: {s1.get_full_name()}")
    print()


if __name__ == "__main__":
    test_student_class()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
STUDENT CLASS RUBRIC (20 points total)

1. Constructor (__init__) - 4 points
   [4] All attributes initialized correctly with private naming convention
   [3] Most attributes initialized, minor issues
   [2] Some attributes initialized
   [1] Constructor exists but major issues
   [0] Constructor not implemented or doesn't work

2. Properties (Getters) - 4 points
   [4] All 6 properties implemented correctly (student_id, first_name, last_name, email, program, year)
   [3] 5 properties working correctly
   [2] 3-4 properties working correctly
   [1] 1-2 properties working
   [0] No working properties

3. Properties (Setters) - 4 points
   [4] All 6 setters implemented with appropriate validation
   [3] 5 setters working correctly
   [2] 3-4 setters working correctly
   [1] 1-2 setters working
   [0] No working setters

4. __str__ Method - 3 points
   [3] Returns properly formatted string exactly as specified
   [2] Returns string with minor formatting issues
   [1] Returns string but wrong format
   [0] Not implemented or doesn't work

5. to_csv_format() Method - 2 points
   [2] Returns properly formatted CSV string matching file format
   [1] Returns CSV but format issues
   [0] Not implemented or doesn't work

6. get_full_name() Method - 1 point
   [1] Returns full name correctly formatted
   [0] Not implemented or doesn't work

7. Documentation - 2 points
   [2] All methods have complete docstrings with author/date
   [1] Most methods documented
   [0] Missing or incomplete documentation

TOTAL: ___ / 20 points

NOTES:
"""
        