from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
comp_sci = Course("Computer Science I")
english = Course("English")


test_student = Student("Phillip", "Antibus")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bruno", "Piyadasa")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("Owen", "Hill")
test_student3.add_course(math)
test_student3.add_course(phys_ed)
test_student3.add_course(comp_sci)
test_student3.add_course(english)

all_students = [test_student, test_student2, test_student3]

print(all_students)

for student in all_students:
    print(f"\n" + str(student))
    
"""
 for this part you may need to review the other skeleton code to:
    - see how to get items from a list
    - see if there is code (like a function) in that file you can call in this file
    - verify that running this file gets you the correct output with information from that file
  Also, review syntax of pulling items from a list from other activities 
"""
