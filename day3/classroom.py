#a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (___init___) 
#and define a method that returns the full name of the person as a combined string.
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname 
    def whatsyourname(self):
        name = self.firstname + ' ' +  self.lastname
        return name

#b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor 
#and define a method that prints the full name and the subject area of the student.
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject 
    def whatsyourstudent(self):
        print(self.firstname+ ' ' + self.lastname + ', ' + self.subject)

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def whatsyourprof(self):
        print(self.firstname+ ' ' + self.lastname + ', ' + self.course)

