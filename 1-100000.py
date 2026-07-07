import pathlib

fajl = pathlib.Path("text_files.py/1-100000.txt")
A = []

for i in range(1, 100001):
    A.append(str(i))

for i in A:
    fajl.write_text(text,i)
print("Done")   