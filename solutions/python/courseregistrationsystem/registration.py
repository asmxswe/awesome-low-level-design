import datetime

from course import Course
from student import Student


class Registration:
    def __init__(self, student: Student, course: Course, registration_time: datetime):
        self.student = student
        self.course = course
        self.registration_time = registration_time
