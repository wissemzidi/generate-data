from random import randint
from generator import generate,generateName

data = open("data.js", "w")
data.writable()

lenData = int(input("len data: "))

data.write("let users = {\n")
for i in range (lenData) :
  lenName = randint(5, 8)
  lenPassword = randint(12, 16)
  l1 = "  user" + str(i) + ": {"
  l2 = '    name: "' + generateName(lenName) + '",'
  l3 = '    email: "' + generate(lenPassword) + '@gmail.com",'
  l4 = '  },'
  data.write("" + l1 +"\n")
  data.write("" + l2 +"\n")
  data.write("" + l3 +"\n")
  data.write("" + l4 +"\n")

data.write("};")

data.close()