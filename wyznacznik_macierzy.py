import random
import numpy as np

for i in range(3):
    a = int(input("Podaj wymiar a macierzy:"))
    b = int(input("Podaj wymiar b macierzy:"))
    M = np.random.randint(0,500,(a,b))
    print(M)
    if a != b:
        print("Nie mozna obliczyc wyznacznika - macierz nie jest kwadratowa")
    else:
        detM = np.linalg.det(M)
        print("Wyznacznik macierzy", detM)
        break
