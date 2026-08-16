def prosecna_potrosnja(*gorivo, kilometraza):
    prosek = gorivo / (kilometraza / 100)
    print(prosek)
    return round(prosek, 2)
     
kilometraza = int(input("Molimo unesite vasu kilometrazu(duzinu relacije): "))
gorivo = int(input("Unesite ukupnu kolicinu potrosenog goriva: "))
prosecna_potrosnja(gorivo, kilometraza)
