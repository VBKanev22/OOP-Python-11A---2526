from task4.person import Person
from task4.student import Student

p = Person("Ivan", 30)
s1 = Student("Maria", 15, 9, "PMG")
s2 = Student("Georgi", 17, 11, "TUES")

print(p.get_info())
print(s1.get_info())
print(s2.get_info())

p.birthday()
s1.birthday()

print(p.get_info())
print(s1.get_info())
