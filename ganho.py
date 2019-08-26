from math import log

raiz = float(input("Entropia do nó acima desse: "))
qtd = int(input("Quantidade total de elementos: "))
qtd_elem = int(input("Quantidade de estados: "))

ganho = 0
for i in range(qtd_elem):
    x = int(input(f"quantidade do estado {i}: "))
    entropia = float(input(f"Entropia desse estado {i}: "))
    ganho += ((x/qtd) * entropia)


print(raiz - ganho)
