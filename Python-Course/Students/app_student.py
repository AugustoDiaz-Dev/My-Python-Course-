#Topic: import a class.

from students import Student #From students file import Student class

student_01 = Student("George", "Bussiness", 3.1, False)
student_02 = Student("Layla", "Art", 3.6, True)

print(student_01.name)
print(student_02.major)
print(student_01.on_honor_roll())
print(student_02.on_honor_roll())
