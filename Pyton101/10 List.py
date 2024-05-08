list = ["apple", "banana", "cherry"]
print(list)

print(len(list))

list1 = ["apple","banana","cherry"]
list2 = [1, 2, 3, 4, 5]
list3 = [True,True,False,False,False]

print(len(list3))

listrandom = ["apple", 1, True, 2,"banana",False]
print(listrandom)
print(len(listrandom))

list = ["apple","banana","cherry"]
print(type(list))

list = [1,2,3,4,5,6,7,8,9,0]
print(list[5])
print(list[0])
print(list[-1])
print(list[2:7])
print(list[:5])
print(list[4:])
print(list[-3:-8])

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("yes apple in your list")
else:
    pass

listC = [1,2,3,4,5]
listC[1] = 9
print(listC)

listC = [1,2,3,4,5]
listC[1:3] = [9,7]
print(listC)

listC = [1,2,3,4,5]
listC[1:4] = [9]
print(listC)

listD = [1,2,3,4,5]
listD.append(6)
print(listD)

listD = [1,2,3,4,5]
listD.insert(1, 6)
print(listD)

listD = [1,2,3,4,5]
listE = [6,7,8,9,0]
listD.extend(listE)
print(listD)

listD = [1,2,3,4,5]
tupleA = (1,2,3)
listD.extend(tupleA)
print(listD)

listE = [1,2,3,4,5,6,7,8,9,0]
listE.remove(1)
print(listE)

listE = [1,2,3,4,5,6,7,8,9,0]
listE.pop(1)
print(listE)

listE = [1,2,3,4,5,6,7,8,9,0]
listE.pop()
print(listE)

listE = [1,2,3,4,5,6,7,8,9,0]
listE.pop()
listE.pop()
print(listE)

listE = [1,2,3,4,5,6,7,8,9,0]
del listE[1]
print(listE)

listE = [1,2,3,4,5,6,7,8,9,0]
listE.clear()
print(listE)

listF = [1,2,3,4,5,6,8,9,0]
for i in listF:
    print(i)

print("--------------------------------------------------------------------")

listF = [1,2,3,4,5,6,8,9,0]
for i in range(len(listF)):
    print(listF[i])

print("--------------------------------------------------------------------")

listf = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(listF):
    print(listF[i])
    i += 1

print("--------------------------------------------------------------------")

listG = ["apple", "banana", "cherry", "kiwi", "mango"]
listH = []
for x in listG:
  if "a" in x:
    listH.append(x)
print(listH)

print("--------------------------------------------------------------------")

listI = [5,6,2,3,8,3,6,2,1,0]
listI.sort()
print(listI)

print("--------------------------------------------------------------------")

listI = [1,2,3,4,5,6,7,8,9,0]
listI.sort(reverse = True)
print(listI)

print("--------------------------------------------------------------------")

def f(n):
    return abs(n - 1)

listI = [1,2,3,4,5,6,7,8,9,0]
listI.sort(key = f)
print(listI)

print("--------------------------------------------------------------------")

listJ = ["banana", "Orange", "Kiwi", "cherry"]
listJ.sort(key = str.lower)
print(listJ)

print("--------------------------------------------------------------------")

listJ = ["banana", "Orange", "Kiwi", "cherry"]
listJ.sort(key = str.upper)
print(listJ)

print("--------------------------------------------------------------------")

listK = [1,2,3,4,5]
listL = [6,7,8,9,0]
listK = listL.copy()
print(listK)
print(listL)

print("--------------------------------------------------------------------")

listM = [1,2,3,4,5]
listN = [6,7,8,9,0]
listO = listM + listN
print(listO)

print("--------------------------------------------------------------------")

list1 = [-1,-2,-3]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list