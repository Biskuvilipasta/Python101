i = lambda a : a +10
print(i(5))

i = lambda a,b : a * b
print(i(5, 6))

i = lambda a,b,c : a + b + c
print(i(5,6,7))

def myfunc(i):
    return lambda a : a * i

mydoubler = myfunc(2)
print(mydoubler(11))

def my_func1(i):
    return lambda a: a * i

mytripler = my_func1(3)
print(mytripler(11))

def my_func2(i):
    return lambda a : a * i

mydoubler = my_func2(2)
mytripler = my_func2(3)

print(mydoubler(11))
print(mytripler(11))

