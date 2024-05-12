class MyClass:
    i = 5
    print(i)
    
MyClass()

p1 = MyClass()
print(p1.i)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Person("Alperen", 20)

print(p1.name)
print(p1.age)
print(p1.name,p1.age)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Alperen", 20)
print(p1)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 =Person("Alperen",20)
print(p1)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)
    
    def printage(self):
        print(self.age)

p1 = Person("Alperen", 20)
p1.myfunc()
p1.printage()

class Person:
    def __init__(randomobject, name, age):
        randomobject.name = name
        randomobject.age = age
    
    def myfunc(abc):
        print("Hello my name is " + abc.name)
    
    def printage(abc):
        print(abc.age)

p1 = Person("Alperen",20)
p1.myfunc()
p1.printage()
p1.age = 40
p1.printage()

del p1.age
del p1

class Person:
    pass
