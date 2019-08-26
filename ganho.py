from math import log

raiz = float(input("Entropia do nó acima desse: "))
qtd = int(input("Quantidade de elementos: "))
qtd_elem = int(input("Quantidade de estados: "))

ganho = 0
for i in range(qtd_elem):
    x = int(input(f"quantidade do estado {i}: "))
    entropia = float(input("Entropia desse estado: "))
    ganho += ((x/qtd) * entropia)
    print(ganho)


print(raiz)
print(ganho)
print(raiz - ganho)
