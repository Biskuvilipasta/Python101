def my_function():
    print("Hello, World!")

my_function()

def my_func(name):
    print("Hello" + name)

my_func("Alperen")
my_func("Ahmet")  

def my_func1(name1, name2):
    print(name1 + " " + name2)

my_func1("Alperen","Sevim")

def my_func2(*name):
    print("3. isim: " + name[2])

my_func2("Alperen", "Ahmet", "Mehmet")

def my_func3(name1,name2,name3):
    print("ilk isim: "+ name1)

my_func3(name1 = "Alperen", name2 = "Ahmet", name3 = "Mehmet")

def my_func4(**name1):
    print("soyad: " + name1["name2"])

my_func4(name = "Alperen" , name2 = "Sevim")

def my_func5(country = "Turkiye"):
    print("I am from " + country)

my_func5()
my_func5("Azerbaijan")
my_func5("Greece")

def my_func6(food):
    for i in food:
        print(i)

fruits = ["Apple", "Banana", "Cherry"]

my_func6(fruits)

def my_func7(i):
    return 5 * i

print(my_func7(3))
print(my_func7(5))
print(my_func7(9))

def my_func8():
    pass

my_func8()

def my_func9(i, /):
    print(i)
    
my_func9(3)

def my_func10(i):
    print(i)
    
my_func10(i = 3)

def my_func11(*, i):
    print(i)
    
my_func11(i = 3)

def my_func12(i):
    print(i)

my_func12(3)

def my_func13(a, b , / , *, c , d):
    print(a + b + c + d)

my_func13(5,6, c = 7, d = 8)

def tri_recursion(i):
  if(i > 0):
    result = i + tri_recursion(i - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)