mytuple = ("Apple", "Banana", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "Alperen"
myit = iter(mystr)

for i in mystr:
    print(next(myit))
    
mytuple = ("Apple", "Banana", "Cherry")

for i in mytuple:
    print(i)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        i = self.a
        self.a += 1
        return i

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        i = self.a
        self.a += 1
        return i

myclass = MyNumbers()
myiter = iter(myclass)

for i in myiter:
    print(i)

