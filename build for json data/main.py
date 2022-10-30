from random import randint
from generator import generate, generateName

data = open("data.json", "w")

lenData = int(input("len data: "))

data.write("{ \n")
for i in range(lenData):
    lenName = randint(4, 8)
    lenPassword = randint(4, 10)
    l1 = '  "' + generateName(lenName) + '": {'
    l2 = '    "Email": "' + generate(lenPassword) + '@gmail.com",'
    l3 = '    "Password": "' + generate(lenPassword) + '"'
    l4 = "  },"
    data.write("" + l1 + "\n")
    data.write("" + l2 + "\n")
    data.write("" + l3 + "\n")
    data.write("" + l4 + "\n")

data.write("}")

data.close()
