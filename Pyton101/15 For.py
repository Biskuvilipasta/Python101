list = [1,2,3,4,5,6,7,8,9,0]
for i in list:
    print(i)

liststr = ["abc", "def", "ghj"]
for i in "def":
    print(i)

list = [1,2,3,4,5,6,7,8,9,0]
for i in list:
    print(i)
    if i == 5:
        break

list = [1,2,3,4,5,6,7,8,9,0]
for i in list:
    if i == 8:
        break
    print(i)

list = [1,2,3,4,5,6,7,8,9,0]
for i in list:
    if i == 4:
        continue
    print(i)
    
for i in range(10):
    print(i)
    
for i in range(2,10):
    print(i)

for i in range(2,10,4):
    print(i)

for i in range(10):
    print(i)
else:
    print("Finish")

for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("Finish")

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]

for i in list1:
    for k in list2:
        print(i,k)

for i in [0 , 1, 2]:
    pass

