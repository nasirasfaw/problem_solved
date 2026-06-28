import sys
 
n = int(input())
poly = [line.strip() for line in sys.stdin]
 
total = 0
for s in poly:
    if s == "Tetrahedron":
        total += 4
    elif s == "Cube":
        total += 6
    elif s == "Octahedron":
        total += 8
    elif s == "Dodecahedron":
        total += 12
    elif s == "Icosahedron":
        total += 20
print(total)
