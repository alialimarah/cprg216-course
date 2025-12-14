"""
Course Class - Course Registration System
==========================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Humza Khan - 000947358
Ali Alimarah - 000964330
Date Completed: December 10, 2025

PURPOSE:
Represents a single course in the system with course information,
instructor details, and capacity limits.

RESPONSIBILITIES:
- Store course information (code, name, instructor, credits, capacity)
- Provide access to course data through properties
- Format course information for display and file storage
- Track enrollment count
- Validate course data

DATA FILE FORMAT (courses.csv):
course_code,course_name,instructor,credits,capacity
CPRG216,Python Programming,Dr. Anderson,3,30

"""


class Course:
    def __init__(self, course_code=None, course_name=None, instructor=None,
                 credits=None, capacity=None):
        """
        Initialize a Course object.

        Author: [Humza Khan]
        Date: [Dec 07]
        Version: 1.0
        """
        self._course_code = None
        self._course_name = None
        self._instructor = None
        self._credits = None
        self._capacity = None
        self._enrolled_count = 0

        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.credits = credits
        self.capacity = capacity

    @property
    def course_code(self):
        """
        Get the course code.

        Author: [Humza Khan]
        Date: [Dec 07]
        """
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        """
        Set the course code.

        Author: [Ali Alimarah]
        Date: [Dec 07]
        """
        if value is None:
            self._course_code = value
            return
        self._course_code = str(value).upper()

    @property
    def course_name(self):
        """
        Get the course name.

        Author: [Ali Alimarah]
        Date: [Dec 07]
        """
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        """
        Set the course name.

        Author: [Humza Khan]
        Date: [Dec 09]
        """
        self._course_name = value

    @property
    def instructor(self):
        """
        Get the instructor name.

        Author: [Humza Khan]
        Date: [Dec 09]
        """
        return self._instructor

    @instructor.setter
    def instructor(self, value):
        """
        Set the instructor name.

        Author: [Ali Alimarah]
        Date: [Dec 09]
        """
        self._instructor = value

    @property
    def credits(self):
        """
        Get the number of credits.

        Returns:
            int: Number of credits (1-4)

        Author: [Ali Alimarah]
        Date: [Dec 09]
        """
        return self._credits

    @credits.setter
    def credits(self, value):
        """
        Set the number of credits.

        Author: [Humza Khan]
        Date: [Dec 10]
        """
        if value is None:
            self._credits = value
            return

        value = int(value)
        if value < 1 or value > 4:
            raise ValueError("Credits must be between 1 and 4")
        self._credits = value

    @property
    def capacity(self):
        """
        Get the course capacity.

        Returns:
            int: Maximum number of students

        Author: [Humza Khan]
        Date: [Dec 10]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Set the course capacity.

        Parameters:
            value (int): New maximum capacity

        Raises:
            ValueError: If capacity is negative

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        if value is None:
            self._capacity = value
            return

        value = int(value)
        if value < 0:
            raise ValueError("Capacity must be 0 or greater")
        self._capacity = value

    @property
    def enrolled_count(self):
        """
        Get the number of students currently enrolled.

        Returns:
            int: Current enrollment count

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        return self._enrolled_count

    def set_enrolled_count(self, count):
        """
        Set the current enrollment count.

        Used by EnrollmentManager to update enrollment numbers.

        Parameters:
            count (int): New enrollment count

        Author: [Humza Khan]
        Date: [Dec 10]
        """
        self._enrolled_count = int(count)

    def is_full(self):
        """
        Check if the course is at capacity.

        Returns:
            bool: True if enrolled_count >= capacity, False otherwise

        Author: [Humza Khan]
        Date: [Dec 10]
        """
        if self.capacity is None:
            return False
        return self.enrolled_count >= self.capacity

    def get_available_seats(self):
        """
        Get the number of available seats in the course.

        Returns:
            int: Number of seats remaining (capacity - enrolled_count)

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        if self.capacity is None:
            return 0
        return self.capacity - self.enrolled_count

    def __str__(self):
        """
        Return a formatted string representation of the course.

        Returns:
            str: Formatted course information

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        return f"[{self.course_code}] {self.course_name} - {self.instructor} ({self.credits} credits) [{self.enrolled_count}/{self.capacity} enrolled]"

    def to_csv_format(self):
        """
        Format course data for CSV file storage.

        Returns:
            str: CSV-formatted string

        Author: [Ali Alimarah]
        Date: [Dec 10]
        """
        return f"{self.course_code},{self.course_name},{self.instructor},{self.credits},{self.capacity}"


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_course_class():
    """Test the Course class implementation."""
    print("=" * 70)
    print("TESTING COURSE CLASS")
    print("=" * 70)
    print()

    # Test 1: Create course with all parameters
    print("Test 1: Creating course with all parameters...")
    c1 = Course("CPRG216", "Python Programming", "Dr. Anderson", 3, 30)
    print(f"✓ Course created: {c1}")
    print()

    # Test 2: Test property access
    print("Test 2: Testing property access...")
    print(f"  Course Code: {c1.course_code}")
    print(f"  Course Name: {c1.course_name}")
    print(f"  Instructor: {c1.instructor}")
    print(f"  Credits: {c1.credits}")
    print(f"  Capacity: {c1.capacity}")
    print(f"  Enrolled: {c1.enrolled_count}")
    print()

    # Test 3: Test enrollment tracking
    print("Test 3: Testing enrollment tracking...")
    c1.set_enrolled_count(12)
    print(f"  Enrolled Count: {c1.enrolled_count}")
    print(f"  Available Seats: {c1.get_available_seats()}")
    print(f"  Is Full? {c1.is_full()}")
    print()

    # Test 4: Test full capacity
    print("Test 4: Testing full capacity...")
    c1.set_enrolled_count(30)
    print(f"  Enrolled Count: {c1.enrolled_count}")
    print(f"  Available Seats: {c1.get_available_seats()}")
    print(f"  Is Full? {c1.is_full()}")
    print()

    # Test 5: Test CSV format
    print("Test 5: Testing CSV format...")
    c2 = Course("DMIT1508", "Database Fundamentals", "Dr. Kim", 3, 35)
    print(f"  CSV: {c2.to_csv_format()}")
    print()


if __name__ == "__main__":
    test_course_class()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
COURSE CLASS RUBRIC (20 points total)

1. Constructor (__init__) - 3 points
   [3] All attributes initialized correctly including enrolled_count
   [2] Most attributes initialized, minor issues
   [1] Constructor exists but major issues
   [0] Constructor not implemented or doesn't work

2. Properties (Getters) - 4 points
   [4] All 6 properties implemented correctly (course_code, course_name, instructor, credits, capacity, enrolled_count)
   [3] 5 properties working correctly
   [2] 3-4 properties working correctly
   [1] 1-2 properties working
   [0] No working properties

3. Properties (Setters) - 4 points
   [4] All 5 setters implemented with appropriate validation
   [3] 4 setters working correctly
   [2] 2-3 setters working correctly
   [1] 1 setter working
   [0] No working setters

4. Enrollment Methods - 3 points
   [3] is_full() and get_available_seats() work correctly
   [2] Both implemented but minor issues
   [1] One method working
   [0] Not implemented or doesn't work

5. __str__ Method - 2 points
   [2] Returns properly formatted string exactly as specified
   [1] Returns string but format issues
   [0] Not implemented or doesn't work

6. to_csv_format() Method - 2 points
   [2] Returns properly formatted CSV string matching file format
   [1] Returns CSV but format issues
   [0] Not implemented or doesn't work

7. Documentation - 2 points
   [2] All methods have complete docstrings with author/date
   [1] Most methods documented
   [0] Missing or incomplete documentation

TOTAL: ___ / 20 points

NOTES:
"""
