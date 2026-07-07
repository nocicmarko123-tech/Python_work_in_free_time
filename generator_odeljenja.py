import random

k = 0
znanje = 0
lista = []

for i in range(1,27):
    lista.append(i)

while True:
    k = random.choice(lista)
    znanje += 1
    if k == 17:
        break

print("Imas pre random tebe:", znanje)