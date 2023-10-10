class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
    

def sort_students(student_list):

  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students



students = [
  Student("Hari", "A123", 7.8),
  Student("Ravi", "A124", 8.9),
  Student("Srini", "A125", 9.1),
  Student("Saurabh", "A126", 9.2),
]

sorted_students = sort_students(students)


for Student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(Student.name, Student.roll_number, Student.cgpa))