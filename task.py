# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

class Student:
  def __init__(self, name, surname, average):
    self.name = name
    self.surname = surname
    self.average = average

def calculate_average(grades):
    average = 0
    for grade in grades:
      average += grade
    return average/len(grades)
    

class Class:
  def __init__(self, name, class_average):
    self.students = []
    self.name = name
    self.class_average = class_average

  def add_student_to_class(self, name, surname, average):
    student = Student(name, surname, average)
    self.students.append(student)

def class_average(students) :
  average = 0
  for student in students:
    average += student.average
  return average/len(students)


class School:
  def __init__(self, name, school_average):
    self.classes = []
    self.name = name
    self.school_average = school_average

  def add_class_to_school(self, name, class_average):
    class1 = Class(name, class_average)
    self.classes.append(class1)


class Schools:
  def __init__(self):
    self.schools =[]


  def add_class_to_school(self, name):
    school = School(name)
    self.cschools.append(school)


#if __init__ == __main__:
class1 = Class("IIIb", 0)
grades = [4, 5, 6, 2, 1, 6, 2]
average = calculate_average(grades)
class1.add_student_to_class("Maria", "Mazur", average)
for student in class1.students:
  print(student.name)
  print(student.surname)
  print(student.average)
