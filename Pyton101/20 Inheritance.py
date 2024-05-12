class Person:
    def __init__(self, name1 , name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname, self.lastname)

i = Person("Alperen","Sevim")
i.printname()

class Student(Person):
    pass

i = Student("Alperen","Sevim")
i.printname()

class Student(Person):
    def __init__(self, name1, name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname)
    
    def printlastname(self):
        print(self.lastname)

p1 = Student("Alperen", "Sevim")
p1.printname()
p1.printlastname()

class Person:
    def __init__(self,name1,name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, name1,name2):
        Person.__init__(self, name1, name2)

i = Student("Alperen", "Sevim")
i.printname()

class Person:
    def __init__(self, name1 ,name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,name1,name2):
        super().__init__(name1,name2)

i = Student("Alperen", "Sevim")
i.printname()

class Person:
    def __init__(self, name1 ,name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname,self.firstname)

class Student(Person):
    def __init__(self,name1,name2):
        super().__init__(name1,name2)

i = Student("Alperen", "Sevim")
i.printname()

class Person:
    def __init__(self, name1,name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,name1,name2):
        super().__init__(name1, name2)
        self.graduationyear = 2025

i = Student("Alperen", "Sevim")
print(i.graduationyear)
print(i.firstname , i.lastname,  i.graduationyear)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

i = Student("Mike", "Olsen", 2025)
print(i.graduationyear)
print("---------------------")
print(i)
print(Student)
print("---------------------")

class Person:
    def __init__(self,name1,name2):
        self.firstname = name1
        self.lastname = name2
    
    def printname(self):
        print(self.firstname, self.lastname)
    
class Student(Person):
    def __init__(self, name1 ,name2 , year):
        super().__init__(name1,name2)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

i = Student("Alperen","Sevim", 2025)
i.welcome()