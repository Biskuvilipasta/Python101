import mymodule
import platform
from mymodule import person1

def greeting(name):
    print("Hello "+ name)

mymodule.greeting("Alperen")

person1 = {
  "name": "Alperen",
  "age": 20,
  "country": "Turkiye"
}

a = mymodule.person1["age"]
print(a)

a = mx.person["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform)
print(x)

def greeting(name):
    print("Hello, "+ name)

person1 = {
    "name": "Alperen",
    "age": "20",
    "country": "Turkiye"    
}
print (person1["age"])
