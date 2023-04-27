from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        # Calling "print(student)"" from main.py will call this method instead
        display_student = f"{self.first_name} {self.last_name} is currently enrolled in: "
        # TODO add a loop that will go through the course list
        for course in self.courses:
            # TODO Add code here to create a string representation of a student,
            # including first and last name and all courses that student is taking
            display_student += f"\n\t {course}"
        return display_student
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        # TODO add code to append new_course to self.courses
        self.courses.append(new_course)
        print(f"{self.courses[-1]} was added to {self.first_name} {self.last_name}'s course list.")
