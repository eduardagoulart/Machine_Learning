from math import log

x = int(input("Quantidade total: "))
yes = int(input("QUantidade de sim: "))
no = int(input("Quantidade de no: "))

entropia = -(yes/x * log(yes/x, 2)) - (no/x * log(no/x, 2))
print(entropia)
