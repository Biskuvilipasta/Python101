dict1 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
print(dict1)
print(dict1["brand"])
print(len(dict1))

dict2 = {
  "brand": "Fiat",
  "electric": False,
  "year": 1996,
  "colors": ["red", "white", "blue"]
}

print(type(dict1))
print(type(dict2))

dict3 = dict(name = "Alperen", age = 55, country = "Turkiye")
print(dict3)
print(dict3)

x = dict3["name"]
y = dict3.get("age")
print(x)
print(y)
print(str(x) + " " +str(y))


car = {
"brand": "Fiat",
"model": "Tofas",
"year": 1996
}
x = car.keys()
print(x) 
car["color"] = "white"
print(x)

x = dict3.values()
print(x)

x = dict3.items()
print(x)

car = {
    "brand":  "Fiat",
    "model": "Tofas",
    "electric": False,
    "LPG": True,
    "color": "Red",
    "year": "1996"    
}

x = car.items()
print(x)

car["KM"] = 312421
print(x)


dict4 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
if "model" in dict4:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5["year"] = 2000
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5.update({"year": 2002})
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5["color"] = "red"
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5.update({"color": "red"})

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5.pop("model")
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5.popitem()
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
del dict5["model"]
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict5.clear()
print(dict5)

dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
for i in dict5:
    print(i)
    
for i in dict5.values():
    print(i)

for i in dict5.keys():
    print(x)

for i, k in dict5.items():
    print(i,k)
    
dict5 = {
    "brand": "Fiat",
    "model": "tofas",
    "year":  1996
}
dict6 = {
    "brand": "mercedes",
    "model": "AMG",
    "year":  2022
}
dict5 = dict6.copy()
print(dict5)
print(dict6)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary