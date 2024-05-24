import re

txt = "Hello, World Python users"
x = re.search("^Hello.*users$", txt)
print(x)

txt = "Hello, World Python users"
x = re.findall("yt", txt)
print(x)

txt = "Hello, World Python users"
x = re.findall("Goodbye",txt)
print(x)

txt = "as bayrakları as"
x = re.findall("as", txt)
print(x)

txt = "Hello World Python users"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

import re

txt = "Hello World Python users"
x = re.search("Goodbye", txt)
print(x)

txt = "Hello World Python users"
x = re.split("\s",txt)
print(x)

txt = "Hello World Python users"
x = re.split("\s", txt, 1)
print(x)

txt = "Hello World Python users"
x = re.sub("\s", "9", txt)
print(x)

txt = "Hello World Python users"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "Hello World Python users"
x = re.search("ai", txt)
print(x)

txt = "Hello World Python users"
x = re.search(r"\bs\w+", txt)
print(x.span())

txt = "Hello World Python users"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "Hello World Python users"
x = re.search(r"\bS\w+",txt)
print(x.group())