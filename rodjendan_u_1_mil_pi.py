import pathlib

sadrzaj = pathlib.Path("text_files.py/sadrzaj.txt")
fajl = sadrzaj.read_text()
linije = [linija.strip() for linija in fajl.splitlines()]
string = ""
godina = int(input("Unesite ddmmgg: "))

for linija in linije:
    string += linija

if str(godina) in string:
    print("Datum se nalazi u broju pi u 1 milion cifri.")
    print("Broj pozicije: ", string.find(str(godina)))
else:
    print("Datum se ne nalazi u broju pi u 1 milion cifri.")