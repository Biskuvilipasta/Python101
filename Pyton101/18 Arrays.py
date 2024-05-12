cars = ["Ford", "Volvo","Toyota"]
print(cars)

car1 = "Ford"
car2 = "Volvo"
car3 = "Toyota"

i = cars[1]
print(i)

cars[0] = "Mercedes"

print(len(cars))
i = len(cars)
print(i)
print(cars)

for i in cars:
    print(i)

cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("Toyota")
print(cars)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list