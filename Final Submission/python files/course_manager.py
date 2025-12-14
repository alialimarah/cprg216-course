"""
CourseManager Class - Course Registration System
=================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 11, 2025

PURPOSE:
Manages the collection of all courses in the system. Handles loading/saving
course data from/to CSV file and provides CRUD operations for courses.

RESPONSIBILITIES:
- Load course data from courses.csv file
- Save course data back to courses.csv file
- Add new courses to the system
- Remove courses from the system
- Search for courses by code or name
- Display course information
- Edit existing course information
- Update enrollment counts

FILE DEPENDENCIES:
- courses.csv (data file)
- course.py (Course class)
- enrollments.csv (to count enrollments)

"""

from course import Course


class CourseManager:
    def __init__(self):
        """
        Initialize the CourseManager.

        Creates an empty list of courses and loads data from courses.csv file.

        Author: [Ali Alimarah]
        Date: [Dec 10]
        Version: 1.0
        """
        self._courses = []
        self.read_courses_file()

    @property
    def courses(self):
        """
        Get the list of all courses.

        Returns:
            list: List of Course objects

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        return self._courses

    def read_courses_file(self):
        """
        Read course data from courses.csv and populate the courses list.

        Author: [Humza Khan]
        Date: [Dec 10]
        """
        self._courses = []
        try:
            with open("courses.csv", "r") as file:
                header = file.readline()
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue

                    parts = line.split(",")
                    if len(parts) != 5:
                        continue

                    course_code = parts[0]
                    course_name = parts[1]
                    instructor = parts[2]
                    credits = int(parts[3])
                    capacity = int(parts[4])

                    course = Course(course_code, course_name, instructor, credits, capacity)
                    self._courses.append(course)

        except FileNotFoundError:
            self._courses = []

    def write_courses_to_file(self):
        """
        Write all course data to courses.csv file.

        Writes header line followed by all courses in CSV format.

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        with open("courses.csv", "w") as file:
            file.write("course_code,course_name,instructor,credits,capacity\\n")
            for course in self._courses:
                file.write(course.to_csv_format() + "\n")

    def add_course(self):
        """
        Add a new course to the system through user input.

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        code = input("Enter course code (e.g., CPRG216): ").strip().upper()
        name = input("Enter course name: ").strip()
        instructor = input("Enter instructor name: ").strip()
        credits_text = input("Enter number of credits (1-4): ").strip()
        capacity_text = input("Enter course capacity: ").strip()

        if self.find_course_by_code(code) is not None:
            print(f"Error: Course code {code} already exists.")
            return

        try:
            credits = int(credits_text)
            capacity = int(capacity_text)
            course = Course(code, name, instructor, credits, capacity)
            self._courses.append(course)
            self.write_courses_to_file()
            print(f"Course [{code}] added successfully.")
        except ValueError:
            print("Error: Invalid credits or capacity. Course not added.")

    def remove_course(self):
        """
        Remove a course from the system by course code.

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        code = input("Enter course code to remove: ").strip().upper()
        course = self.find_course_by_code(code)
        if course is None:
            print(f"Error: No course found with code {code}")
            return

        self._courses.remove(course)
        self.write_courses_to_file()
        print(f"Course {course.course_code} - {course.course_name} removed successfully.")

    def search_course_by_code(self):
        """
        Search for a course by its code and display its information.

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        code = input("Enter course code to search: ").strip().upper()
        course = self.find_course_by_code(code)
        if course:
            self.display_course_info(course)
            return course

        print(f"Error: No course found with code {code}")
        return None

    def search_courses_by_name(self):
        """
        Search for courses by name and display results.

        Searches for partial matches in course names (case-insensitive).

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        term = input("Enter course name to search: ").strip().lower()
        matches = []
        for course in self._courses:
            if term in course.course_name.lower():
                matches.append(course)

        if len(matches) == 0:
            print(f"No courses found matching '{term}'")
            return

        print("\n" + "=" * 92)
        print("COURSE SEARCH RESULTS")
        print("=" * 92)
        print(f"{'Code':<10}{'Course Name':<30}{'Instructor':<18}{'Credits':<9}{'Enrolled':<9}{'Capacity':<9}{'Status':<8}")
        print("-" * 92)
        for course in matches:
            status = "Full" if course.is_full() else "Open"
            print(f"{course.course_code:<10}{course.course_name:<30}{course.instructor:<18}{course.credits:<9}{course.enrolled_count:<9}{course.capacity:<9}{status:<8}")
        print("=" * 92)
        print(f"Matches: {len(matches)}")

    def edit_course_info(self):
        """
        Edit an existing course's information.

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        code = input("Enter course code to edit: ").strip().upper()
        course = self.find_course_by_code(code)
        if course is None:
            print(f"Error: No course found with code {code}")
            return

        new_name = input("Enter new course name (or press Enter to skip): ")
        if new_name.strip() != "":
            course.course_name = new_name.strip()

        new_instructor = input("Enter new instructor (or press Enter to skip): ")
        if new_instructor.strip() != "":
            course.instructor = new_instructor.strip()

        new_credits = input("Enter new credits 1-4 (or press Enter to skip): ")
        if new_credits.strip() != "":
            try:
                course.credits = int(new_credits.strip())
            except ValueError:
                print("Error: Invalid credits. Credits not updated.")

        new_capacity = input("Enter new capacity (or press Enter to skip): ")
        if new_capacity.strip() != "":
            try:
                course.capacity = int(new_capacity.strip())
            except ValueError:
                print("Error: Invalid capacity. Capacity not updated.")

        self.write_courses_to_file()
        print(f"Course {course.course_code} updated successfully!")

    def display_course_info(self, course):
        """
        Display detailed information for a single course.

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        status = "Full" if course.is_full() else "Available"
        print("=" * 42)
        print("COURSE INFORMATION")
        print("=" * 42)
        print(f"Course Code:  {course.course_code}")
        print(f"Course Name:  {course.course_name}")
        print(f"Instructor:   {course.instructor}")
        print(f"Credits:      {course.credits}")
        print(f"Capacity:     {course.capacity}")
        print(f"Enrolled:     {course.enrolled_count}")
        print(f"Available:    {course.get_available_seats()}")
        print(f"Status:       {status}")
        print("=" * 42)

    def display_courses_list(self):
        """
        Display all courses in a formatted table.

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        print("=" * 92)
        print("COURSE LIST")
        print("=" * 92)
        print(f"{'Code':<10}{'Course Name':<30}{'Instructor':<18}{'Credits':<9}{'Enrolled':<9}{'Capacity':<9}{'Status':<8}")
        print("-" * 92)
        for course in self._courses:
            status = "Full" if course.is_full() else "Open"
            print(f"{course.course_code:<10}{course.course_name:<30}{course.instructor:<18}{course.credits:<9}{course.enrolled_count:<9}{course.capacity:<9}{status:<8}")
        print("=" * 92)
        print(f"Total Courses: {len(self._courses)}")

    def get_course_count(self):
        """
        Get the total number of courses in the system.

        Returns:
            int: Number of courses

        Author: [Humza Khan]
        Date: [Dec 11]
        """
        return len(self._courses)

    def find_course_by_code(self, course_code):
        """
        Find and return a course by its code (helper method for other classes).

        Returns:
            Course or None: The Course object if found, None otherwise

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        code = str(course_code).upper()
        for course in self._courses:
            if course.course_code.upper() == code:
                return course
        return None

    def update_enrollment_counts(self, enrollment_manager):
        """
        Update enrollment counts for all courses based on actual enrollments.

        Author: [Ali Alimarah]
        Date: [Dec 11]
        """
        for course in self._courses:
            count = enrollment_manager.get_enrollment_count_for_course(course.course_code)
            course.set_enrolled_count(count)


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_course_manager():
    """Test the CourseManager class implementation."""
    print("=" * 70)
    print("TESTING COURSE MANAGER CLASS")
    print("=" * 70)
    print()

    # Test 1: Initialize and load data
    print("Test 1: Initialize CourseManager...")
    manager = CourseManager()
    print(f"✓ Manager created")
    print(f"  Courses loaded: {manager.get_course_count()}")
    print()

    # Test 2: Display all courses
    print("Test 2: Display all courses...")
    manager.display_courses_list()
    print()

    # Test 3: Find course by code
    print("Test 3: Find course by code...")
    course = manager.find_course_by_code("CPRG216")
    if course:
        print(f"✓ Found: {course}")
        manager.display_course_info(course)
    print()


if __name__ == "__main__":
    test_course_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
COURSE MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 4 points
   [4] Correctly initializes list and loads from file with error handling
   [3] Loads data but minor issues
   [2] Loads data but significant issues
   [1] Constructor exists but doesn't load properly
   [0] Not implemented or doesn't work

2. File Writing - 2 points
   [2] Correctly writes all courses to CSV file
   [1] Writes to file but format issues
   [0] Not implemented or doesn't work

3. Add Course Method - 3 points
   [3] Prompts for all info, checks duplicates, adds to list, saves
   [2] Works but missing some functionality
   [1] Partially working
   [0] Not implemented

4. Remove Course Method - 2 points
   [2] Finds course, removes, saves, appropriate messages
   [1] Works but issues
   [0] Not implemented

5. Search Methods - 3 points
   [3] Both search methods work correctly
   [2] Both work but minor issues
   [1] One works correctly
   [0] Not implemented

6. Edit Course Method - 2 points
   [2] Allows editing all fields, handles empty input, saves
   [1] Works but issues
   [0] Not implemented

7. Display Methods - 2 points
   [2] Both display methods format correctly
   [1] Display works but formatting issues
   [0] Not implemented

8. Helper Methods - 2 points
   [2] find_course_by_code() and update_enrollment_counts() work
   [1] One method works
   [0] Not implemented

TOTAL: ___ / 20 points

NOTES:
"""
