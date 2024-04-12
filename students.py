#basic Project 1 for deeper understanding of the arrays (DSA)

class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

students = []

def add_student(name, age, grade):
  student = Student(name, age, grade)
  students.append(student)

def remove_student(name):
  for student in students:
    if student.name == name:
      students.remove(student)
      return


def update_students(name, age=None, grade=None):
  for student in students:
    if student.name == name:
      if age is not None:
        student.age = age
      if grade is not None:
        student.grade = grade
      return  



def display_students():
  for student in students:
    print(f"Name: {student.name}, Age: {student.age}, Grade:{student.grade} ")

add_student("1. Ranu", 17, "B")
add_student("2. Nikra", 16, "C")
add_student("3. Dhanajay", 19, "A")
add_student("4. Manyra", 32, "A")
add_student("5. Niki", 16, "C")
add_student("6. Kamra Vedi", 19, "F")


update_students("4. Manyra", 23, "F")



display_students()



