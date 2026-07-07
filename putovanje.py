k = []

for i in range(4):
    a1,b1 = map(int,input().split())
    kilo = a1 + b1
    k.append(kilo)

k.sort()
putacetri = k[1]*4
zbir = sum(k)
razlika = zbir - putacetri
impostor = k[1] + razlika
print(k.index(impostor)+1)